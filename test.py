from typing import Text
import cv2
import pytesseract
import  imutils
import numpy as np
import time
import pandas as pd


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_text(img):
    #img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    img = np.array(img)
    img = imutils.resize(img, width=500)
    cv2.imshow("car.jpeg", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 170, 200)

    cnts= cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
    NumberPlateCnt = None 

    count = 0
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
                NumberPlateCnt = approx 
        break

    # Masking the part other than the number plate
    mask = np.zeros(gray.shape,np.uint8)
    new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
    new_image = cv2.bitwise_and(img,img,mask=mask)
    cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
    cv2.imshow("Final_image",new_image)

    # Configuration for tesseract
    config = ('-l eng --oem 1 --psm 3')

    # Run tesseract OCR on image
    data = pytesseract.image_to_string(new_image, config=config)
    #print(data)


    #Data is stored in CSV file
    raw_data = {'date': [time.asctime( time.localtime(time.time()) )],'v_number': [data]}

    df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
    df.to_csv('data.csv')

        
    return data


# if __name__ == "__main__":
#     img_1 = cv2.imread('car.jpeg', cv2.IMREAD_UNCHANGED)
#     txt = extract_text(img_1)
#     print(txt)
        