import os
import subprocess
from celery import Celery


CELERY_BROKER_URL = os.envvar['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.envvar['CELERY_RESULT_BACKEND']

celery = Celery('arachni')
celery.conf.broker_url = CELERY_BROKER_URL
celery.conf.result_backend = CELERY_RESULT_BACKEND


def call_scanner(args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr


@celery.task
def run_scan(args):
    stdout, stderr = call_scanner(args)
    return stdout or stderr
