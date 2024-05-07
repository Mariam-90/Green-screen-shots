#HW1


import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) != 4:
        print("Usage: python program_name.py img_filename bk_filename ofilename")
        return

    img_filename = sys.argv[1]
    bk_filename = sys.argv[2]
    ofilename = sys.argv[3]

    green_screen_img = cv2.imread(img_filename)
    background_img = cv2.imread(bk_filename)

    # Resize background image to match the size of the green screen image
    if green_screen_img.shape[:2] != background_img.shape[:2]:
        background_img = cv2.resize(background_img, (green_screen_img.shape[1], green_screen_img.shape[0]))

    # Convert green screen image to HSV
    hsv_green_screen = cv2.cvtColor(green_screen_img, cv2.COLOR_BGR2HSV)

    # Calculate the mean of green pixels in the image
    green_pixels = hsv_green_screen[:, :, 0][(hsv_green_screen[:, :, 0] >= 40) & (hsv_green_screen[:, :, 0] <= 80)]
    mean_hue = np.mean(green_pixels)

    # Define range around the mean hue for green color in HSV
    hue_range = 20
    lower_green = np.array([mean_hue - hue_range, 40, 40])     
    upper_green = np.array([mean_hue + hue_range, 255, 255])  

    # Create mask for green color
    mask = cv2.inRange(hsv_green_screen, lower_green, upper_green)

    # Invert the mask
    mask_inverse = cv2.bitwise_not(mask)

    # Use bitwise operations to combine the images
    foreground = cv2.bitwise_and(green_screen_img, green_screen_img, mask=mask_inverse)
    background = cv2.bitwise_and(background_img, background_img, mask=mask)
    result = cv2.add(foreground, background)

    # Save the result
    cv2.imwrite(ofilename, result)

    # Show the images by using matplotlib
    plt.figure(figsize=(15, 10))
    
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(green_screen_img, cv2.COLOR_BGR2RGB))
    plt.title('GreenScreen Image')
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(cv2.cvtColor(background_img, cv2.COLOR_BGR2RGB))
    plt.title('BackGround Image')
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('Result')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
