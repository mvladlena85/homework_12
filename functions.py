import json


def load_data_from_json_file() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


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


#save_post("imggggg", "bla-bla-bla")
