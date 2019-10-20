# -*- coding: utf-8 -*-


class Router:
    METHODS = ['GET', 'PATCH', 'DELETE', 'POST', 'UPDATE']

    def __init__(self):
        self.db = {}

    def __getattr__(self, attr):
        if attr.upper() in self.METHODS:
            return lambda path: self.execute_method(attr.upper(), path)
        raise AttributeError(f"{self} instance has not {attr} attribute")

    def add_path(self, path, method, func):
        if path in self.db.keys():
            return 'This path already exists'
        else:
            self.db[path] = [method, func]
            return 'Done'

    def execute_method(self, method, path):
        if path not in self.db.keys():
            return error_404(path, method)
        elif method not in self.db[path]:
            return error_405(path, method)
        else:
            func = self.db[path][-1]
            return func(path, method)


def my_info(path, method):
    return 200, {'me': 'Joanne'}


def update_me(path, method):
    return 200, 'OK'


def remove(path, method):
    return 200, 'deleted'


def modify(path, method):
    return 200, 'patched'


def replace(path, method):
    return 200, 'putted'


def create(path, method):
    return 200, 'posted'


def error_404(path, method):
    return 404,  'Error 404: Not Found'


def error_405(path, method):
    return 405, 'Error 405: Method Not Allowed'


if __name__ == '__main__':
    router = Router()
    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/your', 'UPDATE', update_me))
    print(router.update('/your'))
