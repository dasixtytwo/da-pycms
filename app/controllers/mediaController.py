from app.models.Media import Media
from app.controllers.postController import PostController
from mongoengine.queryset import DoesNotExist


class MediaController(object):
    @staticmethod
    def get_by_ids(ids):
        return Media.objects(id__in=ids)

    @staticmethod
    def get(**kwargs):
        try:
            return Media.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def delete(**kwargs):
        try:
            medias = Media.objects(**kwargs)

            for _media in medias:
                posts = PostController.get_all(
                    query={'medias': _media}
                )

                for post in posts:
                    if _media in post.medias:
                        post.medias.remove(_media)

                    post.update(medias=post.medias)

            return medias.delete()
        except DoesNotExist:
            return False

    @staticmethod
    #returns all media inside db as list of Media objects
    def get_all(order_by='-created_at', offset=None, limit=None, query={}):
        _all = Media.objects(**query).skip(offset)\
            .limit(limit).order_by(order_by)

        return _all

    @staticmethod
    def create(**kwargs):
        c = Media(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Media.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
