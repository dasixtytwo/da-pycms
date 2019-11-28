from app.models.Group import Group
from mongoengine.queryset import DoesNotExist
from app.mongo import db


class GroupController(object):
  @staticmethod
  def get_by_ids(ids):
    return db.group.find({
      '_id': {'$in': ids}
    })

  @staticmethod
  def get(**kwargs):
    try:
      return Group.objects.get(**kwargs)
    except DoesNotExist:
      return None
    
  @staticmethod
  def get_all(order_by='-created_at', query={}):
    _all = Group.objects(**query).order_by(order_by)

    return _all

  @staticmethod
  def create(**kwargs):
    c = Group(**kwargs)
    c.save()

    return c

  @staticmethod
  def exist(**kwargs):
    try:
      return Group.objects.get(**kwargs) is not None
    except DoesNotExist:
      return False

