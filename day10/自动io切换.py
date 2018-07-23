
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(6)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(3)
    print('Implicit context switch back to bar')

def func3():
    print("running func3 ")
    gevent.sleep(1)
    print("running func3  again ")

gevent.joinall([
    gevent.spawn(foo),#生成一个协程
    gevent.spawn(bar),
    gevent.spawn(func3),
])


