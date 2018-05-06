from django.core.management import call_command
from uwsgidecorators import cron

__all__ = ('crawling_new_book',)


@cron(minute=0, hour=2, day=-1, month=-1, dayweek=-1, )
def crawling_new_book():
    call_command('crawling_new_book')
