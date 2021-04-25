import io
from PIL import Image
from flask import Flask, render_template, request, jsonify
from base64 import b64decode
import add_sign

app = Flask(__name__)

files = {
  '1': 'https://storage.yandexcloud.net/www.documents.com/docs_uploaded/consent_personal_data_JohnSmith.docx',
  '2': 'http://www.yandex.ru',
}

@app.route('/')
def home():
  url_option = request.args.get('url')
  url_link = files.get(url_option)
  if not url_link:
    url_link = 'https://storage.yandexcloud.net/www.documents.com/consent_personal_data.docx'
  return render_template('index.html', url=url_link)


# @app.route('/saveSignature', methods=['POST'])
# def save_signature():
#    signature = request.form.get('signature')
#    sign_b64 = ''.join(signature.split(',')[1])
#
#    with open('signature.png', 'wb') as f:
#      f.write(base64.decodestring(sign_b64.encode()))
#   add_sign.sign_doc("JohnSmith")
#
#
#   return jsonify(success=True)

@app.route('/saveSignature', methods=['POST'])
def save_signature():
  signature = request.json.get('signature', None)

  if not signature:
    raise Exception()

  photo_decoded = b64decode(
    signature[signature.index('base64,') + 7:]
  )
  photo_io = io.BytesIO(photo_decoded)

  with open('signature.png', 'wb') as f:
    f.write(photo_io.getbuffer())

  basewidth = 100
  img = Image.open('signature.png')
  wpercent = (basewidth / float(img.size[0]))
  hsize = int((float(img.size[1]) * float(wpercent)))
  img = img.resize((basewidth, hsize), Image.ANTIALIAS)
  img.save('signature_resized.png')

  add_sign.sign_doc("JohnSmith")

  return jsonify(success=True)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
