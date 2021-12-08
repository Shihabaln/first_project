# Plate number extractor
This project is intended to be used with speed cameras to detect and record plate numbers. 



## Project demo
* Run `python main.py`



## Dependencies
* Flask
* OpenCV
* Pandas
* Tesseract 4

## Usage
* `data.csv` will contain the plate numbers extracted in excel sheet
* In `test.py` line 10 ,do change the path to tessetact to where OCR engine is installed. 
* to install `tesseract` for windows first download binary version from https://github.com/UB-Mannheim/tesseract/wiki
* `pip install flask` , `pip install opencv-python` , `pip install pytesseract`

