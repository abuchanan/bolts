import functools
# TODO I haven't figured out the right pattern for this yet


class CustomLogger(logging.getLoggerClass()):
    def task(self, msg):
        """
        A function decorator that logs a given message when the function
        is called, and logs a "Done" message when the function returns.

            log = logging.getLogger('example')

            @log.task('Running foo')
            def foo():
                ...do something...
                return 'bar'

            print foo()

        The example would output:
            INFO:example:Running foo
            bar
            INFO:example:Running foo:Done
        """
        def decorator(fn):
            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                self.info(msg)
                ret = fn(*args, **kwarg)
                self.info(msg + ':Done')
                return ret
            return wrapped
        return decorator
            
