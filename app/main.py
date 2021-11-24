from typing import Optional
import random
import string

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = "!#$%&*+,-./:;=?@^_|"
all_chars = lower + upper + num + symbols
all_chars = lower + upper + num + symbols

@app.get("/password", response_class=HTMLResponse)
def get_pass():

    passwords = {
        length: "".join(random.sample(all_chars, length))
        for length in range(6,20)
    }
    ret = "Longueur | Mot de passe\n"
    for length in range(6,20):
        ret += f"{length:>8} | {passwords[length]}\n"

    return "<html><code style='white-space: pre;'>" + ret + "</code></html>"


@app.get("/concierge")
def get_concierge():
    candidates = ["Adrien", "Matthieu", "Yoann"]
    return random.choice(candidates)
