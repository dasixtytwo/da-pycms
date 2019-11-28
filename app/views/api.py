from flask import ( 
    Blueprint, 
    request, 
    jsonify 
)
from app.controllers.pageController import PageController
from app.controllers.mediaController import MediaController
from app.session_utils import login_required
from bson.objectid import ObjectId


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/page/update/<page_id>', methods=['POST', 'GET'])
@login_required
def update_page(page_id):
    if request.method == 'POST':
        query_object = request.get_json()

        kwargs = {
            'data': query_object
        }

        page = PageController.get(id=ObjectId(page_id))
        page.update(**kwargs)
        page = PageController.get(id=ObjectId(page_id))

        return jsonify(page.data)


@bp.route('/page/data/<page_id>')
def show_page(page_id):
    page = PageController.get(id=ObjectId(page_id))

    return jsonify(page.data)


@bp.route('/media/delete/<media_id>')
def show_media_delete(media_id):
    return jsonify(MediaController.delete(id=ObjectId(media_id)))
