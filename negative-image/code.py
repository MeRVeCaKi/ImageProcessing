import cv2 
import numpy as np 
image_path = "input.jpg"
def image_to_matrix(image_path):
    img = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb_matrix = np.array(image_rgb)
    height, width, _ = rgb_matrix.shape
    return rgb_matrix, width, height
rgb_matrix, width, height = image_to_matrix(image_path)
print(width)
print(height)
pixel_list = []
for y in range(height):
    row = []
    for x in range(width):
        pixel = rgb_matrix[y,x]
        row.append(list(pixel))
    pixel_list.append(row)
output_file_name = "matrix.txt"
with open(output_file_name, "w") as file:
    for row in pixel_list:
        file.write(str(row) + "\n")
for y in range(height):
    for x in range(width):
        pixel = pixel_list[y][x]
        pixel_list[y][x] = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]
rematrix_image = np.array(pixel_list, dtype=np.uint8)
output_image_path = "output.jpg"
cv2.imwrite(output_image_path, cv2.cvtColor(rematrix_image, cv2.COLOR_RGB2BGR))