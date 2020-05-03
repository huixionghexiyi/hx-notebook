from datetime import datetime
import functools
def log(cmd):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if cmd =='get_time':
                print(datetime.now())
            else:
                print('funk u.')
            return func(*args,**kw)
        return wrapper
    return decorator

@log('get_time')
def do_something(thing):
    print(thing)
do_something('watch tv.')


