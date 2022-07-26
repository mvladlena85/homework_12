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

    return render_template('post_uploaded.html', img="https://images.unsplash.com/photo-1525351326368-efbb5cb6814d"
                                                     "?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2"
                                                     ".1&auto=format&fit=crop&w=580&q=80", text=text)
