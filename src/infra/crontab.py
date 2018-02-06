from uwsgidecorators import cron
from django.core.management import call_command

__all__ = ('ping', )


@cron(minute=0, hour=-1, day=-1, month=-1, dayweek=-1,)
def ping():
    call_command('ping')
