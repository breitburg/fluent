from rocket import __version__

from sys import argv as arguments
from os import mkdir, getcwd
from os.path import join

from yaml import dump

arguments = arguments[1:]


def command():
    if len(arguments) == 0:
        print('❌ No command was specified.\n→ Type help to get list of commands')
    elif arguments[0] == 'version':
        print(f'🚀 Rocket, version {__version__}\n⚡️ Checking for updates unavailable')
    elif arguments[0] == 'doctor':
        print('Don\'t implemented yet 🙁')
    elif arguments[0] == 'new':
        project_name = arguments[1]
        project_directory = join(getcwd(), project_name)

        for directory in [
            project_directory,
            join(project_directory, 'lib')
        ]:
            mkdir(directory)

        open(
            file=join(project_directory, 'manifest.yml'),
            mode='w'
        ).write(
            dump(data=dict(
                name=project_name,
                author='Unknown',
                version='1.0',
                sdk=__version__
            ), default_flow_style=False)
        )

        open(
            file=join(project_directory, 'lib', 'app.py'),
            mode='w'
        ).write('''from rocket.material import *

class MyApp(Widget):
    def build(self):
        return Text('Hello, world')

launch(MyApp())''')

        print(f'💫 Creating new project... ({project_name})')

    elif arguments[0] == 'help':
        print('''List of available commands: 🌚
→ rocket new (name) – Create new project
→ rocket doctor – Check all dependencies availability
→ rocket version – Get information about installed version
→ rocket help – Print this list''')
    else:
        print(f'⚠️  \"{arguments[0]}\" is unknown command!')
