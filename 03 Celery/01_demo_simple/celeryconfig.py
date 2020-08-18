CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = "127.0.0.1"  #IP address of the server running RabbitMQ and Celery
BROKER_PORT = 6379
BROKER_URL = 'redis://'
# FORKED_BY_MULTIPROCESSING = 1

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'greeting-every-10-seconds': {
        'task': 'tasks.show_greeting',
        'schedule': timedelta(seconds=10),
    },
}
