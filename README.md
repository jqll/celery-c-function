### `Celery -P gevent` stops during another thread calling into a long running C++ extension function, even if that function releases GIL.

#### To Reproduce
1. Clone this repo.
2. cd into it.
3. Install the `longsleep` module:
```sh
cd longsleep
python3 setup.py sdist
pip3 install dist/longsleep-1.0.0.tar.gz
```
4. Start Redis
```sh
docker run -d -p 6379:6379 redis
```

5. Start the app
```sh
celery worker -A app:app -P gevent -l info --autoscale=30,10 --prefetch-multiplier 5
```

#### Output
No tasks started when long_sleep is called by another thread. long_sleep is a C++ extension function that sleeps for 20 seconds. It releases the GIL before sleeping.
```
[2020-08-11 02:20:50,866: INFO/MainProcess] Received task: app.test_task[ac35e3d1-7540-4a7b-93f4-b36f5f8d72da]  
[2020-08-11 02:20:55,868: INFO/MainProcess] Task app.test_task[ac35e3d1-7540-4a7b-93f4-b36f5f8d72da] succeeded in 5.000165025005117s: None
[2020-08-11 02:20:55,870: INFO/MainProcess] Received task: app.test_task[55029807-8e29-4277-b552-8936a1b22e5c]  
[2020-08-11 02:21:00,875: INFO/MainProcess] Task app.test_task[55029807-8e29-4277-b552-8936a1b22e5c] succeeded in 5.000175439985469s: None
[2020-08-11 02:21:00,884: WARNING/MainProcess] going to call long_sleep
[2020-08-11 02:21:20,884: WARNING/MainProcess] long_sleep done
[2020-08-11 02:21:20,890: INFO/MainProcess] Received task: app.test_task[0bf4ca81-970f-4d3a-8962-176e5b2d0c69]  
[2020-08-11 02:21:25,891: INFO/MainProcess] Task app.test_task[0bf4ca81-970f-4d3a-8962-176e5b2d0c69] succeeded in 5.000209701946005s: None
[2020-08-11 02:21:25,893: INFO/MainProcess] Received task: app.test_task[c601577a-1bf7-47c2-a9af-64517239c791]  
```

