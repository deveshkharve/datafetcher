import requests
from utils import dbUtils
from utils.utilFunctions import logger

def fetchUrl(link):
    try:
        dbResopnse = dbUtils.getData(link)
        if dbResopnse:
            return 200, dbResopnse

        res = requests.get(link)
        if res.status_code in [ 200, 201 ]:
            dbUtils.setData(link, res.text)
            return 200, res.text
        else:
            return res.status_code, None
    except Exception as e:
        logger.error(e)
        return 500, 'Error Occured while fetching data'
