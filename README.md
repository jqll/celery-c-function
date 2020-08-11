### `Celery -P gevent` stops during another thread calls into a long running C++ extension function, even if that function releases GIL.

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
No tasks started when long_sleep is called by another thread:
```
[2020-08-11 01:20:12,974: INFO/MainProcess] Received task: app.test_task[84ead87a-ffc4-4aa3-8ca8-db904a3da3f5]  
[2020-08-11 01:20:17,979: INFO/MainProcess] Task app.test_task[84ead87a-ffc4-4aa3-8ca8-db904a3da3f5] succeeded in 5.000351045979187s: None
[2020-08-11 01:20:17,988: WARNING/MainProcess] going to call long_sleep
[2020-08-11 01:21:57,989: WARNING/MainProcess] long_sleep done
[2020-08-11 01:21:57,994: INFO/MainProcess] Received task: app.test_task[2ae520dc-69da-4dee-a15e-0155865e7d08]  
[2020-08-11 01:22:02,995: INFO/MainProcess] Task app.test_task[2ae520dc-69da-4dee-a15e-0155865e7d08] succeeded in 5.00021721702069s: None
```

