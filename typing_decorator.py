# coding: utf-8 -*-


def typed(func, strict=True):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__.values()

        if strict:              # <= convert_upper
            new_args = []
            list_of_annotations = [ann for ann in annotations][:-1]
            for index, arg in enumerate(args):
                if not isinstance(arg, list_of_annotations[index]):
                    raise TypeError('Arguments required to be as in annotations')
                new_args.append(arg.upper())
            return func(*new_args)

        elif annotations:       # <= add
            format_args = []
            list_of_annotations = [ann for ann in annotations][:-1]
            list_of_types = [type(i) for i in args]

            for index, i in enumerate(list_of_annotations):
                if isinstance(list_of_types[index], i):
                    format_args.append(args[index])
                else:
                    format_args.append(i(args[index]))

            return func(*format_args)

        else:                   # <= acc
            return func(*args)

    return wrapper


@typed
def decision(a: str, b: str, c: str) -> str:
    return str(a + b + c)


print(decision('3', 'True', '4.2'))
