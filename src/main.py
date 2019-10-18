import json
from difflib import get_close_matches as gcm


def get_data_file(filename):
    with open(filename, "r") as f:
        d = json.load(f)
    return d


prompt_y = ("y", "Y", "yes", "Yes", "YES", "si", "Si", "SI")
prompt_n = ("n", "N", "no", "No", "NO", "nope", "Nope", "NOPE")
prompt_x = ("exit", "Exit", "EXIT", "quit", "Quit", "QUIT", "qqq", "QQQ")

data = get_data_file("data\\data.json")

chkdata = data.keys()


def lookup():
    while True:
        w = input("enter a word >")
        w = w.lower()
        girish = gcm(w, chkdata)
        if w in data:
            return data[w]
        elif len(girish) > 0:
            while True:
                gir = gcm(w, chkdata)[0]
                ans = input("Word not found. Did you mean: %s?" % gcm(w, chkdata)[0])
                if ans in prompt_y:
                    return data[gir]
                elif ans in prompt_n:
                    print("Balls...")
                    break
                elif ans in prompt_x:
                    print("Dude...")
                    exit()
                else:
                    break

        else:
            print("Word not found!")


prog = lookup()

for i in prog:
    if isinstance(i, str):
        print(i)
    elif isinstance(i, list):
        print(str(i))
    else:
        print("wrong?")
