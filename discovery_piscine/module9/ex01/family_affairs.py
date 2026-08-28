#!/usr/bin/env python3

def find_the_redheads(dic):
    # return [f"{k}" for k, v in dic.items() if v == "red"]  
    return list(filter(lambda x: dic[x] == "red", dic.keys()))
  

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))