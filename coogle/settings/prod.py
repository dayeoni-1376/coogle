from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True # 추후에 False로 변경 예정

ALLOWED_HOSTS = [
    '.compute.amazonaws.com',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')