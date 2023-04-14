import qrcode

filename = str(input("Wie soll die Datei heissen?: "))
content = str(input("Was willst du codieren?: "))

qr = qrcode.QRCode()
qr.add_data(content)
img = qr.make_image()
img.save((filename) + ".png")
