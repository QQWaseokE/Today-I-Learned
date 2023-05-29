import cv2
import numpy as np

def detect_cracks(image_path):
    #Load the image
    image = cv2.imread(image_path)
    
    #Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Apply a threshold to convert grayscale to binary image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    #Find contours of cracks
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #Draw red grid on the image
    height, width, _ = image.shape
    cell_size = 44  # Adjust this value to control the grid cell size
    for x in range(0, width, cell_size):
        cv2.line(image, (x, 0), (x, height), (0, 0, 255), 1)
    for y in range(0, height, cell_size):
        cv2.line(image, (0, y), (width, y), (0, 0, 255), 1)
    
    #Count the number of grid compartments containing cracks
    crack_count = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cell_x = x // cell_size
        cell_y = y // cell_size
        cell_width = (x + w) // cell_size - cell_x + 1
        cell_height = (y + h) // cell_size - cell_y + 1
        crack_count += cell_width * cell_height
        cv2.rectangle(image, (cell_x * cell_size, cell_y * cell_size),
                      ((cell_x + cell_width) * cell_size, (cell_y + cell_height) * cell_size),
                      (0, 255, 0), 1)
    
    #Display the image with cracks and grid
    cv2.imshow("Cracks with Grid", image)
    cv2.waitKey(0)
    
    #Return the crack count
    return crack_count

#Provide the path to the image
image_path = "/Users/qqwaseoke/Documents/School/campus/bird/crack.jpeg"

#Call the function to detect cracks and count the compartments
crack_count = detect_cracks(image_path)

#Print the crack count
print("Total grid: 170")
print("Number of grid compartments containing cracks:", crack_count)
rate = (crack_count / 170)*100
print("Crack rate:", round(rate,2),"%")


# 결과
<img width="1676" alt="Screenshot 2023-05-27 at 21 31 46" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/c49d0cf0-97ce-41e5-b589-1d927d4929b3">
