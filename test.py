import cv2
import numpy as np

# Read the binary mask image obtained after thresholding
binary_mask = cv2.imread('watch.jpg', 0)  # Read as grayscale

# Define a kernel for morphological operations (structuring element)
kernel = np.ones((5,5), np.uint8)  # 5x5 square kernel, you can adjust the size

# Perform erosion to remove small noise
eroded_mask = cv2.erode(binary_mask, kernel, iterations=1)

# Perform dilation to restore the character regions
dilated_mask = cv2.dilate(eroded_mask, kernel, iterations=1)

# Alternatively, you can directly perform opening or closing operations
# Opening: Erosion followed by dilation (removes small objects)
opening_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)

# Closing: Dilation followed by erosion (fills small holes)
closing_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, kernel)

# Display the results
cv2.imshow('Original Binary Mask', binary_mask)
cv2.imshow('Eroded Mask', eroded_mask)
cv2.imshow('Dilated Mask', dilated_mask)
cv2.imshow('Opening Mask', opening_mask)
cv2.imshow('Closing Mask', closing_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()