from lib.base.command import BaseCommand


class Command(BaseCommand):
    title = 'PING'
    help = 'PING'

    def run(self, *args, **options):
        self.log_info('PONG...')
