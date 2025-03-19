#!/usr/bin/env python3

import json
import tarfile

furigana_dict = {}


def add_word(word: str, reading: str, furigana: list[dict[str, str]]):
    if word not in furigana_dict:
        furigana_dict[word] = {}

    furigana_dict[word][reading] = mylist = []
    for item in furigana:
        new_item = [item["ruby"]]
        if "rt" in item:
            new_item.append(item["rt"])
        mylist.append(new_item)


with open("./input/JmdictFurigana.json", encoding="utf-8-sig") as json_file:
    furigana_list = json.load(json_file)

    for item in furigana_list:
        add_word(item["text"], item["reading"], item["furigana"])

output_file = "./output/jmdict-furigana-map.json"
with open(output_file, mode="w", encoding="utf-8") as json_file:
    json.dump(furigana_dict, json_file, ensure_ascii=False)
with tarfile.open("./releases/jmdict-furigana-map.json.tar.gz", mode="w:gz") as tar:
    tar.add(output_file)
