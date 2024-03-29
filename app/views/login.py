from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect
)
from app.controllers.userController import UserController
from app.password import check_password


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    err_wrong_cred = 'Wrong credentials'
    errors = []

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing = UserController.get(name=username)

        if not existing:
            errors.append(err_wrong_cred)

        if not len(errors):
            if not check_password(existing['password'], password):
                errors.append(err_wrong_cred)

        if not len(errors):
            session['user_id'] = str(existing.id)

            return redirect('/admin')

    return render_template('admin/login.html', errors=errors)


@bp.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'user_id' in session:
        session['user_id'] = None
        del session['user_id']

    return redirect('/admin/login')
