#!/usr/bin/env python3
import multiprocessing
import gunicorn.app.base
from os import environ, path
from dotenv import load_dotenv
from app import app
from app.utils.log import log_setup


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class FlaskApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(FlaskApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    dotenv_path = path.join(path.dirname(__file__), '.env')
    print(dotenv_path)
    if path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    log_setup(filename='application.log')
    options = {
        'bind': '%s:%s' % (environ.get('APP_HOST'), environ.get('APP_PORT')),
        'workers': number_of_workers(),
    }
    FlaskApplication(app, options).run()




