from app.models.Widget import Widget
from mongoengine.queryset import DoesNotExist
from app.mongo import db


class WidgetController(object):
    @staticmethod
    def get_by_ids(ids):
        return db.widget.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return Widget.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(order_by='-date_start', query={}):
        _all = Widget.objects(**query).order_by(order_by)

        return _all

    @staticmethod
    def create(**kwargs):
        c = Widget(**kwargs)
        c.save()

        return c

    @staticmethod
    def exist(**kwargs):
        try:
            return Widget.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
