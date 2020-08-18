from celery.task import task
import time


@task
def add(x, y):
    return x + y


@task
def add_pause(x, y):
    time.sleep(10)
    return x + y


@task
def show_greeting():
    return "Hello, World!"