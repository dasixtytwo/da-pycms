from app.config import config
import os
import glob
import ntpath
import json


def get_theme_path():
    config = {}
    with open('config.json') as _file:
        config = json.loads(_file.read())

        return config

    _file.close()


def set_theme_path(tp):
    file_path = 'config.json'

    try:
        with open(file_path, 'w+') as _file:
            _file.write(json.dumps(tp, indent=2, sort_keys=True))
        _file.close()
    except ValueError:
        pass

    return tp


def get_theme_templates():
    templates_dir = os.path.join(config['theme_dir'], 'templates')

    if os.path.isdir(templates_dir):
        query = os.path.join(templates_dir, '*.html')

        return [
            {'path': path, 'name': ntpath.basename(path)}
            for path in glob.glob(query)]

    return []


def get_template_path(name):
    for template in get_theme_templates():
        if template['name'] == name:
            return template['path']


def get_theme_db():
    file_path = os.path.join(config['theme_dir'], 'db.json')

    db = {}

    if not os.path.isfile(file_path):
        return db

    try:
        with open(file_path) as _file:
            db = json.loads(_file.read())
        _file.close()
    except ValueError:
        pass

    return db


def set_theme_db(db):
    file_path = os.path.join(config['theme_dir'], 'db.json')

    try:
        with open(file_path, 'w+') as _file:
            _file.write(json.dumps(db, indent=2, sort_keys=True))
        _file.close()
    except ValueError:
        pass

    return db


def get_template_config(name):
    template_config = {}

    config_path = os.path.join(
        config['theme_dir'],
        'templates',
        name.replace('.html', '.json')
    )

    if not os.path.isfile(config_path):
        return None

    with open(config_path) as _file:
        template_config = json.loads(_file.read())
    _file.close()

    return template_config
