# keeping things lightweight, lets use redis for persistent datastorage

import redis
import pymysql
import config as CONFIG
from utils.utilFunctions import logger

r = redis.Redis(host='localhost', port=6379, db=0)


def setData(key, value):
    r.set(key, value)

def getData(key):
    return r.get(key)


hostname = CONFIG.DB['host']
username = CONFIG.DB['username']
password = CONFIG.DB['password']
database = CONFIG.DB['database']


def connection():
    try:
        conn = pymysql.connect(
            host=hostname,
            user=username,
            passwd=password,
            db=database
        )
        logger.info('connected')
        return conn
    except Exception as e:
        logger.info('unable to connect')
        logger.error(e)
        raise(e)



def insertQuery(query):

    my_connection = connection()
    try:
        with my_connection.cursor() as cursor:
            # Create a new record
            sql = query
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
            my_connection.commit()
            return str(cursor.lastrowid)
    except Exception as e:
        logger.error(e)
        raise e
    finally:
        my_connection.close()