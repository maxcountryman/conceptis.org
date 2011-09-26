class Config(object):
    SECRET_KEY = '#\xfa\xaas\\\xf1\xbc\xd8\xf8\x05*\xa5\x80\x9e!f'
    
    SITE_NAME = 'Conceptis'
    SITE_TITLE = 'Max\'s blog about stuff and things | ' + SITE_NAME
    SITE_AUTHOR = 'Max Countryman'
    SITE_DESCRIPTION = 'Max Countryman\'s blog about code, life, and everything else!'
    #LONG_DESCRIPTION = 'This blog is a collection of articles about obversations I\'ve made and stuff I\'m working on.'
    
    GOOGLE_ANALYTICS_UA = 'change me!' 
    
    POSTS_PER_PAGE = 3
    
    SITE_WHITELIST = ['127.0.0.1']


class ConfigDebug(Config):
    DEBUG = True
    EXTERNAL = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flog.db'


class ConfigProduction(Config):
    DEBUG = False
    EXTERNAL = True
    EXTERNAL_HOST = '192.168.0.1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flog.db'

