

import logging
import sys
import random
import time

import graypy

my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('graylog', 12201)
my_logger.addHandler(handler)
my_logger.addHandler(logging.StreamHandler(stream=sys.stdout))

possible_logging_messages = [
    lambda x: my_logger.debug('Debug Graylog.', extra={"x": x}),
    lambda x: my_logger.info('Info Graylog.', extra={"x": x}),
    lambda x: my_logger.warning('Warning Graylog.', extra={"x": x}),
    lambda x: my_logger.error('Error Graylog.', extra={"x": x}),
    lambda x: my_logger.exception('Exception Graylog.', extra={"x": x}),
    lambda x: my_logger.critical('Critical Graylog.', extra={"x": x}),
]


def main():
    while True:
        try:
            b = random.randint(0, 3)
            random.choice(possible_logging_messages)(b)
            print(3/b)
        except Exception:
            my_logger.exception("Uncaught exception")
            my_logger.critical("Uncaught critical exception")
        finally:
            time.sleep(random.uniform(1, 5))


if __name__ == '__main__':
    main()
