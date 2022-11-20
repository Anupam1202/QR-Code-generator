import  qrcode

img = qrcode.make("https://www.linkedin.com/company/sahutechnologies/")
img.save("linkedin.jpg")
