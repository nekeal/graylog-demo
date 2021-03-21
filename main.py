

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
    lambda: my_logger.debug('Debug Graylog.'),
    lambda: my_logger.info('Info Graylog.'),
    lambda: my_logger.warning('Warning Graylog.'),
    lambda: my_logger.error('Error Graylog.'),
    lambda: my_logger.exception('Exception Graylog.'),
]


def main():
    while True:
        try:
            random.choice(possible_logging_messages)()
            b = random.randint(0, 3)
            print(3/b)
        except Exception:
            my_logger.exception("Uncaught exception")
        finally:
            time.sleep(random.uniform(1, 5))


if __name__ == '__main__':
    main()
