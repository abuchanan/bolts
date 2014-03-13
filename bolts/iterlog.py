import functools
import logging


default_log = logging.getLogger(__name__)


def log_iterable(iterable, freq=1000, log=default_log):
    for i, item in enumerate(item, start=1):
        if i % freq == 0:
            msg = format.format(i)
            log.info(msg)
        yield item


def log_generator(generator_fn, *log_args, **log_kwargs):
    @functools.wraps(generator_fn)
    def wrapper(*args, **kwargs):
        generator = generator_fn(*args, **kwargs)
        return log_iterable(generator, *log_args, **log_kwargs)
    return wrapper
