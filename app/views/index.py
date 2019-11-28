from flask import (
    Blueprint,
    request,
    flash
)
from app.controllers.pageController import PageController
from app.controllers.postController import PostController
from app.controllers.mediaController import MediaController
from app.controllers.widgetController import WidgetController
from app.config import config
from app.theme_utils import get_theme_db
from app.editing_utils import admin_navigation
from jinja2 import (
    Environment,
    FileSystemLoader
)
import os
from bson.objectid import ObjectId
from app.forms.ContactMailSettingsForm import ContactMailSettingsForm
from app.utils.sendmail import send_mail


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
)

env = Environment(
    loader=FileSystemLoader(os.path.join(
        config['theme_dir'], 'templates'))
)

env.globals.update(
    admin_navigation=admin_navigation,
    PageController=PageController,
    PostController=PostController,
    MediaController=MediaController,
    WidgetController=WidgetController
)


@bp.route('/<page_name>', methods=['POST', 'GET'])
@bp.route('/', defaults={'page_name': None}, methods=['POST', 'GET'])
def show(page_name):
    page = PageController.get(name=page_name) if page_name\
        else PageController.get(is_startpage=True)

    # Create form for send mail
    form = ContactMailSettingsForm()

    if not page:
        return 'page not found', 404

    j_template = env.get_template(page.template)

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return j_template.render(db=get_theme_db(), page=page, form=form)
        else:
            send_mail(form.name.data, form.email.data, form.message.data)
            message = 'Email has been sent!'
            return j_template.render(db=get_theme_db(), page=page, form=form, success=True, message=message)

    elif request.method == 'GET':
        return j_template.render(db=get_theme_db(), page=page, form=form)


@bp.route('/post/<post_id>')
@bp.route('/', defaults={'post_id': None})
def show_post(post_id):
    post = PostController.get(id=ObjectId(post_id)) if post_id else None

    if not post:
        return 'post not found', 404

    j_template = env.get_template(post.template)

    return j_template.render(db=get_theme_db(), post=post, page=post)
