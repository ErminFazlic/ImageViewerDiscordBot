from flask import Flask
from threading import Thread

app=Flask('')

@app.route('/')
def home():
    return "Heyho"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_running():
  t= Thread(target=run)
  t.start()