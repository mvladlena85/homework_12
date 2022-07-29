from flask import json
from functions import load_data_from_json_file


def save_post(img: str, text: str):
    """
    Функция записи данных в posts.json
    :param img: str
            путь до картинки
    :param text: str
            текст к посту
    :return: None
    """
    data_list = load_data_from_json_file()
    data_list.append({"pic": img,
                      "content": text})

    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False)
