from reloadr import ClassReloadr, get_new_source
from inspect import getmodule
from time import time


def reload_class(target):
    print('⚡️ Performing hot reload...')
    start_time = time()

    source = get_new_source(target, 'class', filepath=None)
    module = getmodule(target)
    locals_ = {}

    try:
        exec(source, module.__dict__, locals_)
    except Exception as exception:
        print(f'⚠️ Hot reload was rejected: {exception.args[0]}')
        return target

    print(f'🤘 Reloaded in {round((time() - start_time) * 1000, 3)}ms')
    return locals_[target.__name__]._target


class AppReloader(ClassReloadr):
    def _reload(self):
        self._target = reload_class(self._target)
        # Replace the class reference of all instances with the new class
        for ref in self._instances:
            instance = ref()  # We keep weak references to objects
            if instance:
                instance.__class__ = self._target


def auto_reload(target):
    result = AppReloader(target)
    result._start_watch_reload()
    return result
