from django.core.management import call_command
from uwsgidecorators import cron


@cron(minute=0, hour=2, day=-1, month=-1, dayweek=-1, )
def crawling_new_book(signum: int):
    call_command('crawling_new_book')
