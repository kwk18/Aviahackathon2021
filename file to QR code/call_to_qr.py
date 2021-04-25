import qrcode
import boto3
data = "https://pastebin.com"
filename = "site.png"
img = qrcode.make(data)
img.save(filename)

