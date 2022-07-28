from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from loader.view import loader_blueprint
from main.view import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Запускаем приложение
app.run()
