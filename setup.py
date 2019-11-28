from setuptools import setup


setup(
    name='dfa-cms',
    version='0.2.5',
    license='MIT',
    description='DFA CMS is a content management system',
    author='Davide Agosti',
    author_email='davide.a@davideagosti.info',
    platforms='any',
    url='http://davideagosti.info/',
    install_requires=[
        'wtforms',
        'flask-assets',
        'flask-ckeditor',
        'flask-bower',
        'pymongo',
        'mongoengine',
        'jsmin',
        'flask',
        'bcrypt'
    ],
    packages=[
        'app'
    ],
    entry_points={
        'console_scripts': [
            'dfacms-init = app.initialize:init'
        ]
    }
)
