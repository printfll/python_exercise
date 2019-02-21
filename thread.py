import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s %(asctime)s',
                    )

def daemon(wait=2):
    logging.debug('Starting')
    time.sleep(wait)
    logging.debug('Exiting')

def non_daemon(wait=0):
    logging.debug('Starting')
    time.sleep(wait)
    logging.debug('Exiting')

def test_1():
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    d.join()
    t.join()
    logging.debug("Continue test_1")
# (daemon    ) Starting 2019-02-20 15:01:41,073
# (non-daemon) Starting 2019-02-20 15:01:41,073
# (non-daemon) Exiting 2019-02-20 15:01:41,083
# (daemon    ) Exiting 2019-02-20 15:01:43,079
# (MainThread) Continue test_1 2019-02-20 15:01:43,081

def test_2():
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    d.join()
    t.start()
    t.join()
    logging.debug("Continue test_2")
# (daemon    ) Starting 2019-02-20 15:02:21,891
# (daemon    ) Exiting 2019-02-20 15:02:23,896
# (non-daemon) Starting 2019-02-20 15:02:23,900
# (non-daemon) Exiting 2019-02-20 15:02:23,903
# (MainThread) Continue test_2 2019-02-20 15:02:23,908

def test_3():
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    logging.debug("Continue test_3")
# (daemon    ) Starting 2019-02-20 15:02:56,873
# (non-daemon) Starting 2019-02-20 15:02:56,873
# (MainThread) Continue test_3 2019-02-20 15:02:56,873
# (non-daemon) Exiting 2019-02-20 15:02:56,885

def test_4():
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    d.join(1)
    t.join()
    logging.debug("Continue test_4")
# (daemon    ) Starting 2019-02-20 15:11:42,948
# (non-daemon) Starting 2019-02-20 15:11:42,949
# (non-daemon) Exiting 2019-02-20 15:11:42,956
# (MainThread) Continue test_4 2019-02-20 15:11:43,950

def test_5():
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=non_daemon, args=(3,))
    d.start()
    t.start()
    logging.debug("Continue test_4")
# (daemon    ) Starting 2019-02-20 15:43:50,598
# (non-daemon) Starting 2019-02-20 15:43:50,598
# (MainThread) Continue test_4 2019-02-20 15:43:50,598
# (daemon    ) Exiting 2019-02-20 15:43:52,603
# (non-daemon) Exiting 2019-02-20 15:43:53,608

# test_1() #two threads run in parallel
# test_2() #two threads run in sequence
# test_3() #without join, mainthread don't wait for other threads
# test_4() #join(time): mainthread wait for 1sec, if thread not finish, mainthread keeps going. if wait for 5sec, same result with test_1
# test_5() #let thread t sleep 3sec. non-daemon thread will always block main thread, so we don't need join() to let main thread wait for it.
# for non-daemon thread, we don't need to explicitly join them.
# 设置为daemon的线程会随着主线程的退出而结束，而非daemon线程会阻塞主线程的退出。