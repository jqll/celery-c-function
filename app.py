# -*- coding: utf-8 -*-
import os
import time
import threading

from longsleep import sleep
from celery import Celery


sleep_thread = threading.Thread(target=sleep.sleep_loop)
sleep_thread.daemon = True
sleep_thread.start()



app = Celery(__name__, broker='redis://localhost')


@app.task()
def test_task():
    start_time = time.time()
    while time.time() - start_time < 5:
        pass
