import json
from logger import logger


def load_data_from_json_file() -> list[dict]:
    """
    Загрузка данных из posts.json
    :return: list[dict]
            Содержимое posts.json
    """
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.critical("File not found")
    except json.JSONDecodeError:
        logger.error("Файл не удается преобразовать")


def get_search_result(key: str) -> list[dict]:
    """
    Функция поиска данных по posts.json
    :param key: str
            Ключевое слово поиска
    :return: list[dict]
            список постов, подходящий по параметрам поиска
    """
    data_list = load_data_from_json_file()
    search_result = []
    for data in data_list:
        if key.lower() in data['content'].lower():
            search_result.append(data)
    return search_result


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
        f.write(str(json.dumps(data_list, ensure_ascii=False)))


# save_post("imggggg", "bla-bla-bla")
