from app.config import config
from pymongo import MongoClient
from mongoengine import connect

#connection db
client = MongoClient(config['db_host'], config['db_port'])
DEFAULT_CONNECTION = connect(config['db_name'], host='mongodb://ds123224.mlab.com:23224', username=config['db_user'], password=config['db_pass'])
db = client[config['db_name']]
db.authenticate(config['db_user'], config['db_pass'])
