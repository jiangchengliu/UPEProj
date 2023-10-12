import qrcode
from PIL import Image
# Generate a QR code
data = input("what is you name:")
qr_code = qrcode.make(data)

# Save the QR code as an image file
qr_code.show()