# dfacms
> A content management system with built-in on-sight page and post editing
> this is in constantly updating.

## How it works
* 0 Create a theme. [how to create a theme](HOW_TO_CREATE_A_THEME.md)
* 1 In your `config.json`, you can chenge the themes folder if you like you must specify where your theme is by changing the `theme_dir` value.
* 2 Login and start creating pages.

## Installation
> Requirements:

* python >= 3.5
* a running instance of MongoDB or a database on mlab host, this code is tested on mongoDB on mlab.com

> First, let us create a config file:

    cp config.default.json config.json

> Edit it using your favourite editor.

### Create a virtualenv on window 10, check virtualenv documentation if you have linux

    virtualenv -p  venv 
    
    venv\Scripts\activate

    # if you want deactivate the virtualenv
    deactivate

### Install dfacms
> Run the setup:

    python setup.py develop

> Run the initialization:

    dfacms-init

> This will create the data for login administrator.

> The login credentials is in your `config.json`

### Start the application

    python run.py

> Now visit [http://localhost:5000/admin](http://localhost:5000/admin)   

