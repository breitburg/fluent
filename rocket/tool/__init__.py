from rocket import __version__
from sys import argv as arguments

arguments = arguments[1:]


def command():
    if arguments[0] == 'version':
        print(f'🚀 Rocket, version {__version__}\n⚡️ Checking for updates temporally unavailable')
    elif arguments[0] == 'doctor':
        print('Don\'t implemented yet 🙁')
