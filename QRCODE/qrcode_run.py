'''
pip freeze: command used in Python to display a list of installed packages and their versions. 

Documentation for qrcode: https://pypi.org/project/qrcode/
'''
import qrcode

# Define the data input for the QR code (YouTube link)
data_input = 'https://www.youtube.com/xxx'

# Setup of QR Code parameters
qr = qrcode.QRCode(
    version=10,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Error correction level
    box_size=5,  # Size of each box in the QR code
    border=4)   # Border size around the QR code

# Adding data to the QR code
qr.add_data(data_input)

# Compile data into a QR code array
qr.make(fit=True)

# Create an image from the QR code array, specifying fill and background colors
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the generated QR code image
qr_image.save("QRCODE/qrcode_youtube.png")

# ////////////////////////////////////

# Example of quickly creating a QR code for a password (not recommended)
password = "1234"
quick_qr = qrcode.make(password)
quick_qr.save('password.png')

