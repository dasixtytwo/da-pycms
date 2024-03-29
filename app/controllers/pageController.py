from app.models.Page import Page
from mongoengine.queryset import DoesNotExist
from app.mongo import db


class PageController(object):
    @staticmethod
    def get_by_ids(ids):
        return db.page.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return Page.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(order_by='order', offset=None, limit=None):
        return Page.objects().skip(offset).limit(limit).order_by(order_by)

    @staticmethod
    def create(**kwargs):
        c = Page(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Page.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
