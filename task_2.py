# Создайте декоратор, который вызывает задекорированную функцию пока
# она не выполнится без исключений (но не более n раз - параметр
# декоратора). Если превышено количество попыток, должно быть
# возбуждено исключение типа TooManyErrors


class TooManyErrors(BaseException):
    def __str__(self):
        return 'TooManyErrors!!!'


def dec(n):
    def dec_in(func):
        def wrapper():
            nonlocal n
            k = 0
            while n:
                if n <= k:
                    raise TooManyErrors()
                else:
                    try:
                        func()
                    except ValueError:
                        print(' Error! ')
                        k += 1
                        continue
                break
            return func

        return wrapper

    return dec_in


@dec(2)
def func():
    m = int(input('Enter a digit(not a string): '))
    a = m + 1
    print(a)
    return a


func()
