from flask import Blueprint, render_template, request
from functions import get_search_result

# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route("/")
def main_page():
    return render_template('index.html')


@main_blueprint.route("/search/")
def get_search_result_page():
    search_key = request.args['s']
    search_results = get_search_result(search_key)
    return render_template('post_list.html', search_param=search_key, search_results=search_results)
