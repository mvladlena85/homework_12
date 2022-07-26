import json
import logging

logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt", encoding='utf-8')

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logging_format = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
console_handler.setFormatter(logging_format)
file_handler.setFormatter(logging_format)


def load_data_from_json_file() -> list[dict]:
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.critical("File not found")
    except json.JSONDecodeError:
        logger.error("Файл не удается преобразовать")


def get_search_result(key: str) -> list[dict]:
    data_list = load_data_from_json_file()
    search_result = []
    for data in data_list:
        if key.lower() in data['content'].lower():
            search_result.append(data)
    return search_result


def save_post(img, text):
    data_list = load_data_from_json_file()
    data_list.append({"pic": img,
                      "content": text})

    with open('posts.json', 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(data_list, ensure_ascii=False)))


# save_post("imggggg", "bla-bla-bla")
