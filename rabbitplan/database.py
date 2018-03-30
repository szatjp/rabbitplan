import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config():
    hostname = os.getenv('HOSTNAME', 'unknown')
    if hostname=='unknown':
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'rabbitdb',
            'USER': 'oa',                      # Not used with sqlite3.
            'PASSWORD': '123321',                  # Not used with sqlite3.
            'HOST': 'localhost',
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    else:      
        service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')
        if service_name:
            engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
        else:
            engine = engines['sqlite']
        name = os.getenv('DATABASE_NAME')
        if not name and engine == engines['sqlite']:
            name = os.path.join(settings.BASE_DIR, 'db.sqlite3')      
        return {
            'ENGINE': engine,
            'NAME': name,
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
            'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
        }
