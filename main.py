# Flask app
# Shihab 

from flask import Flask, request, render_template, send_from_directory
import os
from PIL import Image
import test
from app import app
import pytesseract
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# default access page
@app.route("/")
def main():
    return render_template('index.html')


# upload selected image and forward to processing page
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    filename = upload.filename

    # file support verification
    ext = os.path.splitext(filename)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp") or (ext == ".jpeg") or (ext == ".JFIF"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400

    # save file
    destination = "/".join([target, filename])
    print("File saved to to:", destination)
    upload.save(destination)

    # forward to processing page
    return render_template("processing.html", image_name=filename)


#extract number
@app.route("/extract", methods=["POST"])
def extract():
    filename = request.form['image']
    # open and process image
    target = os.path.join(APP_ROOT, 'static/images')
    destination = "/".join([target, filename])
    img = Image.open(destination)
    #img = cv2.imread(img, cv2.IMREAD_UNCHANGED)

    #extracted = img.transpose(Image.FLIP_LEFT_RIGHT)
    #Extract palte number using extract_text function
    extracted = test.extract_text(img)

    return render_template('extraction.html', msg = 'OCR completed',extracted = extracted)

if __name__ == "__main__":
    app.run()

