from django.core.management.base import BaseCommand
from api.models import TaskList


class Command(BaseCommand):
    help = 'Delete TaskList objects from table'

    def add_arguments(self, parser):
        parser.add_argument('tasklist_ids', nargs='+', help='TaskList ids for delete')

    def handle(self, *args, **kwargs):

        for tasklist_id in kwargs['tasklist_ids']:
            try:
                p = TaskList.objects.get(id=tasklist_id)
                p.delete()
                self.stdout.write(self.style.SUCCESS(f"TaskList id: {tasklist_id} was deleted successfully"))
            except TaskList.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"TaskList id: {tasklist_id} does not exists!"))
