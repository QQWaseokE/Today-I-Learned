import cv2
import numpy as np

#Load the road image
image = cv2.imread('/Users/qqwaseoke/Documents/School/campus/birdd/29_roi_bird.jpg')

#Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#Apply Canny edge detection to detect edges
edges = cv2.Canny(blurred_image, 50, 150)

#Dilate the edges to connect nearby edges
dilated_edges = cv2.dilate(edges, None, iterations=2)

#Find contours in the dilated edges
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Create a mask to store the crack regions
crack_mask = np.zeros_like(gray_image)

#Iterate over the contours and filter based on area and aspect ratio
min_area = 100  # Minimum area of a contour to be considered
min_aspect_ratio = 0.1  # Minimum aspect ratio of a contour to be considered

for contour in contours:
    area = cv2.contourArea(contour)
    x, y, width, height = cv2.boundingRect(contour)
    aspect_ratio = width / float(height)

    if area > min_area and aspect_ratio > min_aspect_ratio:
        # Draw the contour on the crack mask
        cv2.drawContours(crack_mask, [contour], 0, 255, -1)

#Apply the crack mask to the original image
crack_image = cv2.bitwise_and(image, image, mask=crack_mask)

#Calculate the size of the grid in pixels based on 30mm spacing
grid_spacing_mm = 3
pixels_per_mm = 5  # Adjust this value based on the image resolution
grid_spacing_pixels = int(grid_spacing_mm * pixels_per_mm)

#Get the image dimensions
height, width, _ = crack_image.shape

#Create a blank image with the same dimensions as the road image
grid_image = np.zeros((height, width, 3), dtype=np.uint8)

#Draw the vertical grid lines
vertical_grids = 0
for x in range(0, width, grid_spacing_pixels):
    cv2.line(grid_image, (x, 0), (x, height), (0, 0, 255), 1)
    vertical_grids += 1

#Draw the horizontal grid lines
horizontal_grids = 0
for y in range(0, height, grid_spacing_pixels):
    cv2.line(grid_image, (0, y), (width, y), (0, 0, 255), 1)
    horizontal_grids += 1
#Combine the road image with the grid image
grid_overlay = cv2.addWeighted(crack_image, 0.8, grid_image, 0.4, 0)

#Display the road image with the grid overlay
cv2.imshow('Road Image with Grid', grid_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Calculate the total number of grids
total_grids = vertical_grids * horizontal_grids

#Print the total number of grids
print(f"Total number of grids: {total_grids}")

###################################################

#Convert the road image to grayscale
gray_image = cv2.cvtColor(crack_image, cv2.COLOR_BGR2GRAY)

#Initialize the counter for white grid cells
white_grid_count = 0

#Iterate over the grid cells and count white cells
for y in range(0, height, grid_spacing_pixels):
    for x in range(0, width, grid_spacing_pixels):
        cell = gray_image[y:y + grid_spacing_pixels, x:x + grid_spacing_pixels]
        avg_intensity = np.mean(cell)
        if avg_intensity > 200:  # Adjust the threshold as needed
            white_grid_count += 1

#Combine the road image with the grid image
grid_overlay = cv2.addWeighted(crack_image, 0.8, grid_image, 0.4, 0)

#Display the road image with the grid overlay
cv2.imshow('Road Image with Grid', grid_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Print the count of white grid cells
print(f"Number of white grid cells: {white_grid_count}")

####################################################################

#Calculate the size of the grid in pixels based on 30mm spacing
grid_spacing_mm = 3
pixels_per_mm = 5  # Adjust this value based on the image resolution
grid_spacing_pixels = int(grid_spacing_mm * pixels_per_mm)

#Get the image dimensions
height, width, _ = crack_image.shape

#Create a blank image with the same dimensions as the road image
grid_image = np.zeros((height, width, 3), dtype=np.uint8)

#Draw the vertical grid lines
for x in range(0, width, grid_spacing_pixels):
    cv2.line(grid_image, (x, 0), (x, height), (0, 0, 255), 1)

#Draw the horizontal grid lines
for y in range(0, height, grid_spacing_pixels):
    cv2.line(grid_image, (0, y), (width, y), (0, 0, 255), 1)

#Convert the road image to grayscale
gray_image = cv2.cvtColor(crack_image, cv2.COLOR_BGR2GRAY)

#Initialize the counter for white cracks
white_crack_count = 0

#Iterate over the grid cells and count white cracks
for y in range(0, height - grid_spacing_pixels, grid_spacing_pixels):
    for x in range(0, width - grid_spacing_pixels, grid_spacing_pixels):
        cell = gray_image[y:y + grid_spacing_pixels, x:x + grid_spacing_pixels]
        avg_intensity = np.mean(cell)
        if avg_intensity > 200:  # Adjust the threshold as needed
            white_crack_count += 1

#Combine the road image with the grid image
grid_overlay = cv2.addWeighted(crack_image, 0.8, grid_image, 0.4, 0)

#Display the road image with the grid overlay
cv2.imshow('Road Image with Grid', grid_overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Print the count of white cracks in the grid
print(f"Number of white cracks in the grid: {white_crack_count}")

# 결과
![29_roi_bird](https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/044f7c11-a9aa-4039-adf4-8ec1ee804484)<img width="440" alt="KakaoTalk_Photo_2023-05-26-05-15-19" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/32f612b9-058d-40b1-96da-733513bb9345">

Number of white grid cells: 0

Number of white cracks in the grid: 0
