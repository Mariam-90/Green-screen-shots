The readme.txt should include the following information:
 
 * The authors' contact information‫:‬


Description:
This program was created as part of a project for the course "Image Processing and Computer Vision." The program takes a photo of a rectangular page and straightens the photo by performing the following steps:
1. Binarizing the image.
2. Finding the largest contour in the image.
3. Finding the bounding rectangle of the contour with minimum area.
4. Calculating the height and width of the page.
5. Defining the transformation matrix to map the four corners of the page to four corners in the output image.
6. Applying a perspective transformation to the image.
7. Writing the new image to the output path.

Environment:
This program is designed to run on macOS. To compile and run the program, the following requirements are needed:
- Python 3.11.0
- OpenCV package
- Matplotlib package

How to Run Your Program:
1. Install Python 3.11.0.
2. Create a virtual environment: `python -m venv opencv-env` (optional).
   - Activate the environment: `source opencv-env/bin/activate`.
   - Deactivate the environment: `deactivate`.
3. Install the OpenCV package: `pip install opencv-contrib-python matplotlib`.
4. Activate the opencv-env environment: `source opencv-env/bin/activate`.
5. Run the program with two input arguments (image path and output path):
   - Example: `python3 Scanner.py path_input_img path_output_img`.
 - Example: `python.exe Scanner.py path_input_img path_output_img`.
Scanner.py ----- the source code 
path_input_img ------ input folder that contain the images
path_output_img ----- output folder that we save the results in it 



Assumptions:
- A page is the basic object in the image.
- The page photographed is a rectangular page.
- The height of the page is greater than its width.
- The page is brighter than the background on which it was photographed.


