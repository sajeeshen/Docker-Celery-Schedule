from celery import Celery
import logging



CELERY_BROKER_URL = 'redis://redis:6379/0'

app = Celery('tasks', broker=CELERY_BROKER_URL, backend='db+sqlite:///db.sqlite3')

# celery -A app.tasks worker --loglevel=info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

# celery -A app.tasks beat --loglevel=info

@app.task
def check():
    logging.info('So should this')

    print("Hello")


app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "app.tasks.check",
        "schedule": 10.0
    }
}
