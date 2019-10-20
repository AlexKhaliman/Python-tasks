# -*- coding: utf-8 -*-
import re


class Serializer:

    def dump(self, data, f):
        with f:
            if type(data) in PRIMITIVE_TYPES:
                f.write(f"[{data}] {type(data)}")
            elif type(data) in CONTAINER_TYPES:
                a = f"{type(data)}$ "
                for arg in data:
                    a += f"[{arg}] {type(arg)} "
                f.write(a)
            elif type(data) in DICTIONARY:
                a = ''
                for key, value in data.items():
                    a += f"key[{key}] typek[{type(key)}] value[{value}] typev[{type(value)}]"
                f.write(a)

    def load(self, f):
        with f:
            a = f.read()
            if a[0] == '[':
                args = re.findall(r"\[(\w*.?\w*)\]", a)
                types = re.findall(r"\'(\w*)\'\>", a)
                return self.get_type(types[0])(args[0])
            elif a[0] == '<':
                args = re.findall(r"\[(\w*.?\w*)\]", a)
                main_type = re.search(r"\'(\w*)\'\>\$", a).group(1)
                types = re.findall(r"\'(\w*)\'\>[^$]", a)
                return self.get_type(main_type)([self.get_type(types[index])(arg) for index, arg in enumerate(args)])
            elif a[0] == 'k':
                keys = re.findall(r"key\[(\w*.?\w*)\]", a)
                values = re.findall(r"value\[(\w*.?\w*)\]", a)
                type_of_keys = re.findall(r"typek\[\<class '(\w*)'", a)
                type_of_values = re.findall(r"typev\[\<class '(\w*)'", a)

                typed_keys = [self.get_type(type_of_keys[index])(arg) for index, arg in enumerate(keys)]
                typed_values = [self.get_type(type_of_values[index])(arg) for index, arg in enumerate(values)]
                result = {}
                for index, value in enumerate(typed_values):
                    result[typed_keys[index]] = value
                return result

    def get_type(self, types):
        if types == 'str':
            return str
        elif types == 'int':
            return int
        elif types == 'float':
            return float
        elif types == 'complex':
            return complex
        elif types == 'bool':
            return bool
        elif types == 'list':
            return list
        elif types == 'tuple':
            return tuple
        elif types == 'set':
            return set
        elif types == 'frozenset':
            return frozenset


PRIMITIVE_TYPES = [
    int,
    float,
    complex,
    str,
    bool
]

CONTAINER_TYPES = [
    list,
    tuple,
    set,
    frozenset
]

DICTIONARY = [
    dict
]

if __name__ == '__main__':
    data = {1: '2', '3': 4.4}
    serializer = Serializer()
    fw = open("data.txt", 'w')
    fr = open("data.txt", 'r')
    serializer.dump(data, fw)
    print(serializer.load(fr))
