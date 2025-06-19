import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7874207255:AAHpnRakHABD67whsLmNWJNel69FtSRqQf0")
    API_ID = int(os.environ.get("API_ID", "25679601"))
    API_HASH = os.environ.get("API_HASH", "105e12ce694578ac241c66d267caee87")

    # Parse AUTH_USERS into a list of integers
    AUTH_USERS = [int(user_id) for user_id in os.environ.get('AUTH_USERS', '1391520393').split(',')]

    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "rahul"
