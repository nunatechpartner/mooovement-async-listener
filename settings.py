import os

### PostgreSQL ###
POSTGRE_HOST = os.environ['POSTGRE_HOST']
POSTGRE_USERNAME = os.environ['POSTGRE_USERNAME']
POSTGRE_PASSWORD = os.environ['POSTGRE_PASSWORD']
POSTGRE_DATABASE = os.environ['POSTGRE_DATABASE']

### API ###
API_KEY = os.environ['API_KEY']
JWT_SECRET = os.environ['JWT_SECRET']
API_PUSH_URL = 'https://mooovement.actuatech.org/api/v0.1/notifications/push/'
