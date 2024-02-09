import cv2
import numpy as np
def preprocess_image(image):
    
    hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Convert image to HSV 
    lower = np.array([0, 0, 0])  
    upper = np.array([179, 255, 100])
    # mask = cv2.inRange(hsv, lower, upper) #threshholding the image to extract characters , here i am highlighting the parts of image to color we are interested in these highlighted areas are character and rest everything is turned to dark
    
    #removing noise
    shape = np.ones((5, 5), np.uint8)
    hsv = cv2.morphologyEx(hsv, cv2.MORPH_OPEN, shape)
    hsv = cv2.morphologyEx(hsv, cv2.MORPH_CLOSE, shape)
    hsv=cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
    

    return hsv
def segment_characters(image):
     contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #finding countours
     min_area = 100 # doing this to remove noise from contours
     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
     character_boxes = [cv2.boundingRect(cnt) for cnt in filtered_contours]
     # FOR INDIVIDUAL CHARACTERS
     characters = [image[y:y+h, x:x+w] for x, y, w, h in character_boxes]
     
     return characters
image = cv2.imread('2.jpeg')
# Preprocess the image
preprocessed_image = preprocess_image(image)
cv2.imshow("gr",preprocessed_image)
# Segment characters
segmented_characters = segment_characters(preprocessed_image)
for i, char in enumerate(segmented_characters):
    cv2.imshow(f'Character {i+1}', char)
    cv2.imwrite("newimage.png", char)

cv2.waitKey(0)
cv2.destroyAllWindows()
