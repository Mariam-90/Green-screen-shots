import cv2
import numpy as np
import sys

def create_green_mask(image):
    lower_green = np.array([36, 25, 25])  # lower limit
    upper_green = np.array([86, 255, 255])  # upper limit

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_green, upper_green).astype(np.uint8)
    return mask

def apply_bilateral_filter(image):
    # Applying bilateral filter to reduce noise
    filtered_image = cv2.bilateralFilter(image, d=120, sigmaColor=70, sigmaSpace=70)
    return filtered_image

def main():
    img_filename = sys.argv[1]
    bk_filename = sys.argv[2]
    ofilename = sys.argv[3]

    img = cv2.imread(img_filename)
    if img is None:
        print("Error: Unable to load the image.")
        exit()
    # Apply bilateral filter to reduce noise
    #img_filtered = apply_bilateral_filter(img)
    # Create a mask for the green areas
    mask_of_green_color = create_green_mask(img)
    img_background = cv2.imread(bk_filename)
    if img is None:
        print("Error: Unable to load the image.")
        exit()
    #img_background_filtered = apply_bilateral_filter(img_background)
    metrics = img.shape
    resized_background = cv2.resize(img_background, (metrics[1], metrics[0]))
    print(f"resized_background shape: {resized_background.shape}")
    print(f"img_background shape: {img.shape}")
    # Apply bitwise_not to create the inverse mask
    green_mask_background = cv2.bitwise_or(resized_background, resized_background, mask=mask_of_green_color)

    # Apply bitwise_not to create the inverse mask
    green_mask_background_not = cv2.bitwise_not(mask_of_green_color)

    # Apply the masks using bitwise_and
    result = cv2.bitwise_and(img, img, mask=green_mask_background_not)
    result = result.astype(np.uint8)
    # Combine the two results
    final_result = cv2.bitwise_or(result, green_mask_background)

    # Display the original image
    cv2.imshow('Original Image', img)
    # Display the green mask
    cv2.imshow('Green Mask', mask_of_green_color)

    # Display the inverse green mask
    cv2.imshow('Inverse Green Mask', green_mask_background)

    # Display the result after applying the masks
    cv2.imshow('Result After Masks', result)

    # Display the final result
    cv2.imshow('Final Result', final_result)

    # Save the final result
    cv2.imwrite(ofilename, final_result)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

#python how1.py studio.jpg background4.jpg img/out.jpg
