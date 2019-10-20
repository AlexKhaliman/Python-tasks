# [black_Jack](https://github.com/AlexKhaliman/Python-tasks/blob/master/black_jack.py)
Реализована популярная карточная игра **Blackjack**

# [molecule_to_atoms](https://github.com/AlexKhaliman/Python-tasks/blob/master/molecule_to_atoms.py)
*Требуется*:
Написать функцию, которая, принимая как параметр строку - формулу молекулы, возвращала бы атомы из этой молекулы и их количество в виде Dict[str, int]

*Примеры*:

H2O -> {H: 2, O: 1}

Mg(OH)2 -> {Mg: 1, O: 2, H: 2}

K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}

# [typing_decorator](https://github.com/AlexKhaliman/Python-tasks/blob/master/typing_decorator.py)
*Трубется*:
Написать декоратор, который проверял бы тип параметров функции следующим образом:
- При вызове без аргументов осуществлял бы конвертацию параметров и возвращаемого значения в указанные типы

```
@typed
def add(a: int, b: int) -> str:
    return a + b

add("3", 5) -> "8"
add(2.35, True) -> "3"
```

- При вызове с параметром *strict=True* выбрасывал бы исключение при неправильной передаче параметров
```
@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()

convert_upper('abc') -> 'ABC'
convert_upper(5) -> TypeError('`convert_upper` argument `msg` required to be a `str` instance')
```
- Если типы параметров функции не указаны декоратор должен предполагать их тип как *Any*
```
@typed
def acc(a, b, c):
    return a + b + c

acc('a', 'b', 'c') -> 'abc'
acc(5, 6, 7) -> 18
acc(0.1, 0.2, 0.4) -> 0.7000000000000001
```
# [serializer](https://github.com/AlexKhaliman/Python-tasks/blob/master/serializer.py)
*Требуется*:
Реализовать программу, которая позволяла бы сериализовывать и десериализовывать python-объекты в файл и обратно по примеру модулей pickle и json.
# [router](https://github.com/AlexKhaliman/Python-tasks/blob/master/router.py)
*Требуется*:
Реализовать класс простого роутера. Каждый роутер имеет путь и метод доступа к этому пути. Один и тот же путь может иметь несколько методов.

Если же такого пути нет, роутер должен вернуть код ошибки 404 с сообщением *'Error 404: Not Found'*

Если же такой путь есть, но был запрошен неверный метод, роутер должен вернуть 405, *'Error 405: Method Not Allowed'*
# [vector](https://github.com/AlexKhaliman/Python-tasks/blob/master/vector.py)
*Требуется*:
Реализуйте класс, описывающий математический вектор размерности n.
*Примеры*:
Создание и базовые арифметические операции (сложение, вычитание, умножение)

```
>>> Vector(1, 2)
Vector(1, 2)
>>> Vector(5, 6) + Vector(1, 3)
Vector(6, 9)
```
Проверка на валидность операции
```
>>> Vector(1,) + Vector(6, 9, 10)
TypeError: Unsupported operands error - Vectors must be the same dimension
```
Оператор @ для скалярного умножения
```
>>> Vector(1, 2) @ Vector(9, 2)
11
```
Оператор * для умножения на скаляр и векторного умножения
```
>>> Vector(2, 3, -1) * Vector(5, 1, 5)
Vector(16, -15, -13)
```
