from fluent import __version__

from sys import argv as arguments


arguments = arguments[1:]


def command():
    if len(arguments) == 0:
        print('❌ No command was specified\n'
              '→ Type help to get list of commands')
    elif arguments[0] == 'version':
        print(f'🚀 Fluent, version {__version__}')
    elif arguments[0] == 'doctor':
        try:
            from sdl2 import sdlttf, sdlgfx
            print('🥳 All libraries are function successful!')
        except Exception as exception:
            print(f'🔥 Something went wrong!\n→ Exception: {exception.__str__()}')
    elif arguments[0] == 'help':
        print('''List of available commands: 🌚
→ fluent doctor – Check all dependencies availability
→ fluent version – Get information about installed version
→ fluent help – Print this list''')
    else:
        print(f'⚠️  \"{arguments[0]}\" is unknown command!')
