import time
from datetime import datetime

from django.core.management.base import BaseCommand as DjangoBaseCommnad

from lib.utils.format import DateTimeFormat


class BaseCommand(DjangoBaseCommnad):
    title = 'No title'

    def log_error(self, msg: str):
        formatted_msg = '[%s] [%s] %s' % (datetime.now().strftime(DateTimeFormat.YMD_HMS), self.title, msg)
        self.stdout.write(self.style.ERROR(formatted_msg))

    def log_info(self, msg: str):
        formatted_msg = '[%s] [%s] %s' % (datetime.now().strftime(DateTimeFormat.YMD_HMS), self.title, msg)
        self.stdout.write(self.style.SUCCESS(formatted_msg))

    def handle(self, *args, **options):
        self.log_info('Command Start.')

        start_time = time.clock()
        self.run(*args, **options)
        time_taken = time.clock() - start_time

        self.log_info('Command Done.  Time Taken : ' + str(round(time_taken, 1)))

    def run(self, *args, **options):
        raise NotImplementedError
