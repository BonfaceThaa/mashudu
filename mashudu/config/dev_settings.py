from .common_settings import *

DEBUG = True
SECRET_KEY = '%ne=4*psu(&pmhbpxy#_f8)7+%m+epwehfi@59@6s4_9=a*zw%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}