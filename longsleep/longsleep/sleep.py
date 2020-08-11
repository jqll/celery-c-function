from longsleep import longsleep
import time


def sleep_loop():
    for i in range(10):
        time.sleep(5)
        print('going to call long_sleep')
        longsleep.long_sleep()
        print('long_sleep done')




