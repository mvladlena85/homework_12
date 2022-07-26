from flask import Blueprint, render_template, request, send_from_directory
from functions import save_post

UPLOAD_FOLDER = "uploads/images"

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route("/post/", methods=["GET"])
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route("/post_uploaded/", methods=["POST"])
def upload_data():
    picture = request.files.get("picture")
    text = request.values.get("content")
    filename = picture.filename
    path = f"{UPLOAD_FOLDER}/{filename}"
    picture.save(path)
    save_post(path, text)
    return render_template('post_uploaded.html', img=filename, text=text)


@loader_blueprint.route("/post_uploaded/<path:path>")
def show_image(path):
    return send_from_directory(UPLOAD_FOLDER, path)
