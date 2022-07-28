import os
from flask import Blueprint, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from logger import logger

from functions import save_post

UPLOAD_FOLDER = "uploads/images"
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.jpeg']

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route("/post/", methods=["GET"])
def add_post_page():
    """Страница добавления поста"""
    return render_template('post_form.html')


@loader_blueprint.route("/post_uploaded/", methods=["POST"])
def upload_data():
    """Страница успешной загрузки поста"""
    picture = request.files.get("picture")
    text = request.values.get("content")
    filename = secure_filename(picture.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in 'UPLOAD_EXTENSIONS':
            logger.info("Файл - не картинка")

    try:
        path = f"{UPLOAD_FOLDER}/{filename}"
        picture.save(path)
        save_post(path, text)
        return render_template('post_uploaded.html', img=filename, text=text)
    except OSError:
        logger.error("Ошибка при загрузке файла")
        return render_template('post_form.html', text="Ошибка при загрузке поста, попробуйте еще раз")


@loader_blueprint.route("/post_uploaded/<path:path>")
def show_image(path):
    """Загрузка картинки из файлохранилища"""
    return send_from_directory(UPLOAD_FOLDER, path)
