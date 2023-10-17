from flask import Blueprint, request
from werkzeug.utils import secure_filename
import os

read_book_bp = Blueprint('read_book', __name__)


@read_book_bp.route('/')
def read_book():
    if request.method == 'POST':
        file = request.files['file']
        print(request.files)
        file.save(os.path.join('books/', secure_filename(file.filename)))
        return ''
    return ''