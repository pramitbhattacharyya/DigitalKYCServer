# DigitalKYCServer
This is the Server Part Of the Digital KYC Application.
This contains the regex implementation on the text extracted from the image and then it will be verified from the database.
The second part will be implemented in future.
This repository contains two way implementation of the same thing.
One where the text from image is extracted using Google OCR API and the text is sent to the sever for parsing it using regex and then verifying it from the database.
The second one is where the image is sent from the mobile to the server as bitmap image and then python programs are running which will concentrate the part of text in the image as a necessary preprocessing before the image is sent for OCR detection using Tesseract. Then the information is parsed using regex and validated from the database.
