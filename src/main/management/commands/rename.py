from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new django project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # logic to rename the project
        files_to_rename = [
            'core/settings/base.py',
            'core/wsgi.py',
            'core/asgi.py',
            'manage.py'
        ]
        folder_to_rename = 'core'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('core', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)
        
        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed from {} to {}'.format(folder_to_rename, new_project_name)))
        