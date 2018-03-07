from uwsgidecorators import cron
from django.core.management import call_command

__all__ = ('ping', )


@cron(minute=0, hour=2, day=-1, month=-1, dayweek=-1,)
def ping():
    call_command('crawling_new_book')
