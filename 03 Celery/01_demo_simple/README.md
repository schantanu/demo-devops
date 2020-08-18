# Demo_Celery

A simple demo of Celery Asynchronous Task Queue Management in Python.

# Requirements

- Spin up a Redis Docker Container
`docker run --name demo-celery-redis -d -p 6379:6379 -t redis`

- Spin up a Celery Worker
`celery worker -l info -P eventlet`

- Open up a Python Console in the project folder

```
>>> from tasks import add, add_pause
>>> add.delay(13, 40)
>>> add_pause.delay(30, 40)
```

- Check output in the Celery Worker console
