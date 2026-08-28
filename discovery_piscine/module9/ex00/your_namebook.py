#!/usr/bin/env python3

def array_of_names(dic):
    # loops through the dictionary and prints both key and title capitalized
    # res = list(map(lambda kv: f"{kv[0]} {kv[1]}".title(), dic.items()))
    # print(res)

    return [f"{k} {v}".title() for k, v in dic.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))