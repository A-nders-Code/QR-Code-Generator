import qrcode

filename = str(input("Wie soll die Datei heissen?: "))
msg = str(input("Was willst du codieren?: "))

qr = qrcode.QRCode()
qr.add_data(msg)
img = qr.make_image()
img.save((filename) + ".png")