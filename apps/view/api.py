import base64

from flask import (
    Blueprint, request, abort
)

from apps.libs import ocr


api_bp = Blueprint('api', __name__)


@api_bp.route('/ocr', methods=['POST'])
def ocr_handler():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            abort(400, 'please upload a file.')
        image = request.files['file']
        return ocr.image_to_string(image.read())


@api_bp.route('/file', methods=['POST'])
def file_handler():
    if request.method == 'POST':
        file = request.files.get('file')
        image = file.read()
        lang = request.form.get('language', None)
        return ocr.image_to_string(image, lang=lang)


@api_bp.route('/base64', methods=['POST'])
def base64_handler():
    if request.method == 'POST':
        data = request.get_json()
        print('data:', data)
        base64_data = data['base64']
        lang = data['language']
        image = base64.b64decode(base64_data)
        return ocr.image_to_string(image, lang=lang)
