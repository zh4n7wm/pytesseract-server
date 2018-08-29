from flask import (
    Blueprint, request, abort, render_template
)

from apps.libs import ocr


page_bp = Blueprint('page', __name__)


@page_bp.route('/', methods=['GET', 'POST'])
def ocr_page():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            abort(400, 'please upload a file.')
        image = request.files['file']
        return ocr.image_to_string(image.read())
