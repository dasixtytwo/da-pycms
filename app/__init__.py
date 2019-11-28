from app.mongo import db
from app.views.index import bp as index_bp
from app.views.blog import bp as blog_bp
from app.views.admin import bp as admin_bp
from app.views.login import bp as login_bp
from app.views.api import bp as api_bp
from app.views.theme import bp as theme_bp
from app.views.uploads import bp as uploads_bp
from app.theme_utils import get_theme_db
from app.session_utils import get_current_user
from app.media_utils import get_file_type
from flask import Flask
from flask_ckeditor import CKEditor
from flask_bower import Bower

# initializes extensions
ckeditor = CKEditor()
bower = Bower()

# application factory
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'basic'


app.config.update(
    #    mail_settings,
    SECRET_KEY='ad304ee6c57c574e13a3bfd985c9086a',
    TEMPLATES_AUTO_RELOAD=True
)

bower.init_app(app)
ckeditor.init_app(app)


app.register_blueprint(index_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(api_bp)
app.register_blueprint(theme_bp)
app.register_blueprint(uploads_bp)

app.jinja_env.globals.update(
    get_theme_db=get_theme_db,
    get_current_user=get_current_user,
    basestring=str,
    isinstance=isinstance,
    get_file_type=get_file_type
)

db = db
