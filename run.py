import os
from app import app
from flask_assets import (
    Bundle,
    Environment
)

STATIC_DIR = 'app/static'

def run():
    try:
        js = Bundle(
            'wget.js',
            'media_gallery.js',
            'utils.js',
            'app.js',
            filters='jsmin',
            output='js/main.js'
        )

        assets = Environment(app)

        assets.load_path = [
            os.path.join(os.path.dirname(__file__), '{STATIC_DIR}/js'.format(
                STATIC_DIR=STATIC_DIR
            ))
        ]

        assets.register('main_js', js)

        # Run App
        if __name__ == '__main__':
            app.run(host='0.0.0.0')

    except KeyboardInterrupt:
        quit()


run()
