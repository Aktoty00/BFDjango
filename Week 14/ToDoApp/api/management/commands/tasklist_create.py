from django.core.management.base import BaseCommand
from api.models import TaskList


def create_todo_list(num, prefix, status):
    for i in range(num):
        if status:
            TaskList.objects.create(name=f'{prefix}_taskList {i}', description=f'description {i}', status=status)
        else:
            TaskList.objects.create(name=f'{prefix}_taskList {i}', description=f'description {i}')


class Command(BaseCommand):
    help = 'Create fake date for TaskList table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of TaskList for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new TaskList')

        parser.add_argument('-s', '--status', action='store_true', help='Create TaskList with status=to do')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')
        status = kwargs.get('status')

        if not prefix:
            prefix = 'AA'

        if not status:
            status = 'to do'

        create_todo_list(total, prefix, status)
