from flask import Blueprint, render_template, request, send_from_directory
from functions import get_search_result
from logger import logger

UPLOAD_FOLDER = "uploads/images"


# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route("/")
def main_page():
    """Главная страница"""
    return render_template('index.html')


@main_blueprint.route("/search/")
def get_search_result_page():
    """Страница с результатами поиска по ключевой фразе"""
    search_key = request.args['s']
    search_results = get_search_result(search_key)
    logger.info(f'Запрос на поиск по фразе "{search_key}"')
    return render_template('post_list.html', search_param=search_key, search_results=search_results)


@main_blueprint.route("/search/<path:path>")
def show_image(path):
    """Загрузка картинки из файлохранилища"""
    return send_from_directory("", path)
