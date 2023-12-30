from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='45.94.47.66',port=8110)

def keep_alive():
    t = Thread(target=run)
    t.start()
