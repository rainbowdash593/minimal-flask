#!/usr/bin/env python3
from os import path
from app import app
from dotenv import load_dotenv


def run():
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=True, threaded=True)


if __name__ == '__main__':
    dotenv_path = path.join(path.dirname(__file__), '.env')
    if path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    run()

