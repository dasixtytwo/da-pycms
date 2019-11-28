from flask import Blueprint
from jinja2 import (
    Environment,
    FileSystemLoader
)
import os
from app.config import config
from app.theme_utils import get_theme_db
from app.editing_utils import admin_navigation
from app.controllers.pageController import PageController
from app.controllers.postController import PostController

bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates'
)

env = Environment(
    loader=FileSystemLoader(os.path.join(
        config['theme_dir'], 'templates'))
)

env.globals.update(
    admin_navigation=admin_navigation,
    PageController=PageController,
    PostController=PostController,
)


@bp.route('/blog', methods=['POST', 'GET'])
def show():
    page = PageController.get(name='blog')
    posts = PostController.get_all()

    if not page:
        return 'page not found', 404

    j_template = env.get_template(page.template)

    return j_template.render(db=get_theme_db(), page=page, posts=posts)
