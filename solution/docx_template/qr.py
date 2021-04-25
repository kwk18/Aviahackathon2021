import qrcode


def generate(url):
    data = url
    filename = "qr.png"
    img = qrcode.make(data)
    img.save(filename)