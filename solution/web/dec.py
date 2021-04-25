import base64
from PIL import Image
from io import BytesIO

f = open('base64.txt', 'r')
data = f.read()
f.closed

im = Image.open(BytesIO(base64.b64decode(data)))
im.save('image.png', 'PNG')