from flask import Flask, request, Response
import qrcode
import io

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    if not url:
        return "Error: No url provided. Please specify a url."

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    #Convert PIL image to bytes
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    #Create Flask response object
    response = Response(img_io.getvalue(), content_type='image/png')
    return response

if __name__ == '__main__':
    app.run(debug=True)



