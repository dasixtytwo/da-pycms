from flask import (
    Blueprint,
    render_template,
    redirect,
    request
)
from bson.objectid import ObjectId
import datetime
from app.session_utils import (
    login_required,
    get_current_user
)
from app.media_utils import upload_file
from app.theme_utils import (
    get_theme_templates,
    get_theme_db,
    set_theme_db,
    get_template_config,
    get_theme_path,
    set_theme_path
)
from app.forms.AccountSettingsForm import AccountSettingsForm
from app.controllers.pageController import PageController
from app.controllers.postController import PostController
from app.controllers.mediaController import MediaController
from app.controllers.userController import UserController
from app.controllers.groupController import GroupController
from app.controllers.profileController import ProfileController
from app.controllers.widgetController import WidgetController


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/')
@login_required
def show():
    return redirect('/admin/dashboard')


@bp.route('/dashboard')
@login_required
def show_dashboard():
    greet = 'Hi'
    return render_template('admin/dashboard.html', title=greet)


@bp.route('/account-settings', methods=['POST', 'GET'])
@login_required
def show_account_settings():
    user = get_current_user()

    form = AccountSettingsForm(request.form)

    if request.method == 'POST' and form.validate():
        kwargs = {
            'name': form.name.data
        }

        if 'avatar' in request.files:
            filename = upload_file(request.files['avatar'])
            avatar_media = MediaController.create(
                name=form.name.data + '-avatar',
                filename=filename
            )
            kwargs['avatar'] = avatar_media

        user.update(**kwargs)
        user = UserController.get(id=user.id)

    form.name.data = user.name

    return render_template('admin/account_settings.html', form=form, user=user)


@bp.route('profile/<profile_id>', methods=['POST', 'GET'])
@bp.route('/profile', defaults={'profile_id': None}, methods=['POST', 'GET'])
@login_required
def show_profile(profile_id):
    profile = ProfileController.get(
        userID=ObjectId(profile_id)) if profile_id else None
    user = UserController.get_all()

    if profile_id:
        newOrUpdate = 'Update'
    else:
        newOrUpdate = 'Create'

    if request.method == 'POST':

        if request.form.get('submit'):
            userID = request.form.get('user_id')
            firstName = request.form.get('profile-firstname')
            lastName = request.form.get('profile-lastname')
            email = request.form.get('profile-email')
            phone = request.form.get('profile-phone')
            website = request.form.get('profile-website')
            address = request.form.get('profile-address')
            city = request.form.get('profile-city')
            country = request.form.get('profile-country')
            postcode = request.form.get('profile-postcode')

            if not profile:
                profile = ProfileController.create(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    phone=phone,
                    website=website,
                    address=address,
                    city=city,
                    country=country,
                    postcode=postcode,
                    userID=userID
                )
                return redirect('/admin/profile/{}'.format(str(profile.id)))
            else:
                profile.update(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    phone=phone,
                    website=website,
                    address=address,
                    city=city,
                    country=country,
                    postcode=postcode
                )
                profile = ProfileController.get(userID=ObjectId(profile_id))

    return render_template(
        'admin/profile.html',
        newOrUpdate=newOrUpdate,
        profile=profile,
        user=user
    )


@bp.route('/pages')
@login_required
def show_pages():
    pages = PageController.get_all()

    return render_template('admin/pages.html', pages=pages)


@bp.route('/page/<page_id>', methods=['POST', 'GET'])
@bp.route('/page', defaults={'page_id': None}, methods=['POST', 'GET'])
@login_required
def show_page(page_id):
    page = PageController.get(id=ObjectId(page_id)) if page_id else None
    templates = get_theme_templates()
    template_config = None

    if page:
        template_config = get_template_config(page.template)

    if request.method == 'POST':
        if request.form.get('delete'):
            page.delete()
            return redirect('/admin/pages')

        if page:
            if request.form.get('delete-data'):
                page.update(data={})
                page = PageController.get(id=ObjectId(page_id))

        if request.form.get('submit'):
            name = request.form.get('page-name')
            slug = request.form.get('page-name')
            content = request.form.get('page-content')
            template = request.form.get('page-template')
            order = request.form.get('page-order')
            is_startpage = request.form.get('page-is_startpage') is not None
            template_fields = {} if not page else page.fields

            slug = slug.replace(' ', '-').lower()

            for k, v in request.files.items():
                if 'template-field' in k:
                    field_file = request.files.get(k)
                    medianame = k
                    filename = upload_file(field_file)
                    media = MediaController.create(
                        name=medianame,
                        filename=filename
                    )

                    template_fields[k] = media.to_dbref()

            for k, v in request.form.items():
                if 'template-field' in k:
                    template_fields[k] = v

            if not page:
                page = PageController.create(
                    name=name.lower(),
                    slug=slug,
                    content=content,
                    template=template,
                    order=order,
                    is_startpage=is_startpage,
                    fields=template_fields
                )
                return redirect('/admin/page/{}'.format(str(page.id)))
            else:
                page.update(
                    name=name.lower(),
                    slug=slug,
                    content=content,
                    template=template,
                    order=order,
                    is_startpage=is_startpage,
                    fields=template_fields
                )
                page = PageController.get(id=ObjectId(page_id))

    return render_template(
        'admin/page.html',
        template_config=template_config,
        templates=templates,
        page=page
    )


@bp.route('/posts')
@login_required
def show_posts():
    posts = PostController.get_all()

    return render_template('admin/posts.html', posts=posts)


@bp.route('/post/<post_id>', methods=['POST', 'GET'])
@bp.route('/post', defaults={'post_id': None}, methods=['POST', 'GET'])
@login_required
def show_post(post_id):
    post = PostController.get(id=ObjectId(post_id)) if post_id else None
    templates = get_theme_templates()
    medias = MediaController.get_all()
    groups = GroupController.get_all()
    template_config = None

    if post:
        template_config = get_template_config(post.template)

    if request.method == 'POST':
        if request.form.get('delete'):
            post.delete()
            return redirect('/admin/posts')

        if request.form.get('submit'):
            title = request.form.get('post-title')
            slug = request.form.get('post-title')
            content = request.form.get('post-content')
            template = request.form.get('post-template')
            post_group = request.form.get('post-group')
            is_published = request.form.get('post-is_published') is not None
            with_sidebar = request.form.get('post-with_sidebar') is not None
            post_template_fields = {} if not post else post.fields
            new_media_files = request.files.getlist('new-medias')
            new_medias = []

            slug = slug.replace(' ', '-').lower()

            post_group = None if not post_group else post_group

            for k, v in request.form.items():
                if 'post-tmpl-field' in k:
                    post_template_fields[k] = v

            for new_media_file in new_media_files:
                filename = upload_file(new_media_file)
                media = MediaController.create(
                    name=new_media_file.filename,
                    filename=filename
                )
                new_medias.append(media)

            if post:
                new_medias = post.medias + new_medias
            else:
                pass

            if not post:
                post = PostController.create(
                    title=title.lower(),
                    slug=slug,
                    content=content,
                    template=template,
                    group=post_group,
                    is_published=is_published,
                    with_sidebar=with_sidebar,
                    created_at=datetime.datetime.now(),
                    medias=new_medias,
                    fields=post_template_fields
                )
                return redirect('/admin/post/{}'.format(str(post.id)))
            else:
                post.update(
                    title=title.lower(),
                    slug=slug,
                    content=content,
                    template=template,
                    group=post_group,
                    is_published=is_published,
                    with_sidebar=with_sidebar,
                    medias=new_medias,
                    fields=post_template_fields
                )
                post = PostController.get(id=ObjectId(post_id))

    return render_template(
        'admin/post.html',
        templates=templates,
        template_config=template_config,
        medias=medias,
        groups=groups,
        post=post
    )


@bp.route('/group/<group_id>', methods=['POST', 'GET'])
@bp.route('/group', defaults={'group_id': None}, methods=['POST', 'GET'])
@login_required
def show_group(group_id):
    group = GroupController.get(id=ObjectId(group_id)) if group_id else None

    if request.method == 'POST':
        if request.form.get('delete'):
            group.delete()
            return redirect('/admin/group')

        if request.form.get('submit'):
            name = request.form.get('group-name')
            description = request.form.get('group-description')

            if not group:
                group = GroupController.create(
                    name=name,
                    description=description,
                    created_at=datetime.datetime.now()
                )
                return redirect('/admin/group/{}'.format(str(group.id)))
            else:
                group.update(
                    name=name,
                    description=description
                )
                group = GroupController.get(id=ObjectId(group_id))

    return render_template('admin/group.html', group=group)


@bp.route('/groups', methods=['POST', 'GET'])
@login_required
def show_groups():
    groups = GroupController.get_all()

    return render_template('admin/groups.html', groups=groups)


@bp.route('/medias')
@login_required
def show_medias():
    medias = MediaController.get_all()

    return render_template('admin/medias.html', medias=medias)


@bp.route('/media/<media_id>', methods=['POST', 'GET'])
@bp.route('/media', defaults={'media_id': None}, methods=['POST', 'GET'])
@login_required
def show_media(media_id):
    errors = []
    media = MediaController.get(id=ObjectId(media_id)) if media_id else None

    if request.method == 'POST':
        if request.form.get('delete'):
            MediaController.delete(id=ObjectId(media_id))
            return redirect('/admin/medias')

        if request.form.get('submit'):
            name = request.form.get('media-name')
            media_file = request.files.get('media-file')
            filename = None

            kwargs = {
                'name': name
            }

            if media_file:
                try:
                    filename = upload_file(media_file)
                    kwargs['filename'] = filename
                except Exception as e:
                    errors.append(str(e))

            if not len(errors):
                if not media:
                    media = MediaController.create(
                        **kwargs
                    )
                    return redirect('/admin/media/{}'.format(str(media.id)))
                else:
                    media.update(
                        **kwargs
                    )
                    media = MediaController.get(id=ObjectId(media_id))

    return render_template('admin/media.html', media=media, errors=errors)


@bp.route('/theme-db', methods=['POST', 'GET'])
@login_required
def show_theme_db():
    db = get_theme_db()

    if request.method == 'POST':
        if request.form.get('submit'):
            for k, v in request.form.items():
                if k == 'submit':
                    continue

                db[k] = v

            set_theme_db(db)

    return render_template('admin/theme_db.html', db=db)


@bp.route('/theme', methods=['POST', 'GET'])
@login_required
def show_theme_path():
    tp = get_theme_path()

    if request.method == 'POST':
        if request.form.get('submit'):
            for k, v in request.form.items():
                if k == 'submit':
                    continue

                tp[k] = v

            set_theme_path(tp)

    return render_template('admin/theme.html', tp=tp)


@bp.route('/widgets', methods=['POST', 'GET'])
@login_required
def show_widgets():
    widgets = WidgetController.get_all()

    return render_template('admin/widgets.html', widgets=widgets)


@bp.route('/widget/<widget_id>', methods=['POST', 'GET'])
@bp.route('/widget', defaults={'widget_id': None}, methods=['POST', 'GET'])
@login_required
def show_widget(widget_id):
    pages = PageController.get_all()
    widget = WidgetController.get(
        id=ObjectId(widget_id)) if widget_id else None

    if request.method == 'POST':
        if request.form.get('delete'):
            widget.delete()
            return redirect('/admin/widget')

        if request.form.get('submit'):
            title = request.form.get('widget-title')
            subtitle = request.form.get('widget-subtitle')
            date_start = request.form.get('widget-date-start')
            date_end = request.form.get('widget-date-end')
            icon = request.form.get('widget-icon')
            content = request.form.get('widget-content')
            widget_page = request.form.get('widget-page')

            widget_page = None if not widget_page else widget_page

            if not widget:
                widget = WidgetController.create(
                    title=title,
                    subtitle=subtitle,
                    date_start=date_start,
                    date_end=date_end,
                    icon=icon,
                    content=content,
                    page=widget_page
                )
                return redirect('/admin/widget/{}'.format(str(widget.id)))
            else:
                widget.update(
                    title=title,
                    subtitle=subtitle,
                    date_start=date_start,
                    date_end=date_end,
                    icon=icon,
                    content=content,
                    page=widget_page
                )
                widget = WidgetController.get(id=ObjectId(widget_id))

    return render_template(
        'admin/widget.html',
        widget=widget,
        pages=pages
    )


@bp.route('/settings')
@login_required
def show_settings():
    return render_template('admin/settings.html')
