#!/usr/bin/env python3

import json

furigana_dict = {}


with open("./output/furigana_dict.json", mode="w", encoding="utf-8") as json_file:
    json.dump(furigana_dict, json_file, ensure_ascii=False)
