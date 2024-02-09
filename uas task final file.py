import cv2
import numpy as np

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0) #to reduce noise

    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4) #binarizing the image

    return thresh

# Function to segment characters
def segment_characters(image):
    # Find contours
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_area = 100
    max_area = 1000
    filtered_contours = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]

    boxes = [cv2.boundingRect(cnt) for cnt in filtered_contours] #box for filtered counters

    boxes = [cv2.boundingRect(cnt) for cnt in filtered_contours]

    characters = [image[y:y+h, x:x+w] for x, y, w, h in boxes]

    return characters

    image = cv2.imread('1.jpeg')
    preprocess = preprocess(image)
    segmented_characters = segment_characters(preprocess)
    for i, char in enumerate(segmented_characters):
        cv2.imshow(f'Character {i+1}', char)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

