# QR-Code-generator
it will generate qr code by using any link
The code you provided utilizes the qrcode library to generate a QR code. Here's how it works:
Import the qrcode library.
Use the qrcode.make() function to create a QR code. Pass the desired content, in this case, the URL "#", as an argument to the function.
Save the generated QR code image using the img.save() function. Provide the filename "linkedin.jpg" as the argument.
After running this code, a QR code image will be generated and saved as "linkedin.jpg" in the current working directory. This QR code can be scanned to access the LinkedIn company page of Sahutechnologies.
Make sure you have the qrcode library installed before running this code. You can install it using pip:
pip install qrcode
