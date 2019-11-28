from app.models.Profile import Profile
from mongoengine.queryset import DoesNotExist
from app.mongo import db


class ProfileController(object):
  @staticmethod
  def get_by_ids(ids):
    return db.profile.find({
      '_id': {'$in': ids}
    })

  @staticmethod
  def get(**kwargs):
    try:
      return Profile.objects.get(**kwargs)
    except DoesNotExist:
      return None

  @staticmethod
  def get_all(order_by='-firstName', query={}):
    _all = Profile.objects(**query).order_by(order_by)

    return _all

  @staticmethod
  def create(**kwargs):
    c = Profile(**kwargs)
    c.save()

    return c
  
  @staticmethod
  def exist(**kwargs):
    try:
      return Profile.objects.get(**kwargs) is not None
    except DoesNotExist:
      return False