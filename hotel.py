# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
# покупка билета в транспортной компании, или простая РПГ. Создайте
# несколько объектов классов, которые описывают ситуацию Объекты должны
# содержать как атрибуты так и методы класса для симуляции различных действий.
# Программа должна инстанцировать объекты и эмулировать какую-либо
# ситуацию - вызывать методы, взаимодействие объектов и т.д.

class Hotel:
    free_rooms = ['101', '102', '103', '104', '105']
    rented_rooms = []
    booked_rooms = []
    list_of_guests = {}

    def __init__(self, name):
        self.name = name
        self.rentroom = []
        self.bookroom = []

    @staticmethod
    def guests():
        list_of_guests = Hotel.list_of_guests
        print('|    Persons:   |   Rent Rooms: | ')
        for i in list_of_guests.items():
            print('|{:^15}|{:^15}|'.format(i[0], (' '.join(i[1]))))

    def rent_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in Hotel.free_rooms:
                print('This room is not acces, please choose another.')
                for i in Hotel.free_rooms:
                    print(i)
            else:
                Hotel.rented_rooms.append(
                    Hotel.free_rooms.pop(Hotel.free_rooms.index
                                         (n)))
                self.rentroom.append(n)
            Hotel.list_of_guests[self.name] = self.rentroom

    def check_out(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in self.rentroom:
                print(self.name + ' is not rent this room(s). He(she) rent :')
                for i in self.rentroom:
                    print(i)
            else:
                Hotel.free_rooms.append(Hotel.rented_rooms.pop
                                        (Hotel.rented_rooms.index(n)))
                self.rentroom.remove(n)

    def book_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in Hotel.free_rooms:
                print('This room is not acces, please choose another.')
                for i in Hotel.free_rooms:
                    print(i)
            else:
                Hotel.booked_rooms.append(
                    Hotel.free_rooms.pop(Hotel.free_rooms.index(n)))

                self.bookroom.append(n)

    def cancel_book_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in self.bookroom:
                print('This room is not booked.')
                for i in Hotel.booked_rooms:
                    print(i)
            else:
                Hotel.free_rooms.append(Hotel.booked_rooms.pop
                                        (Hotel.booked_rooms.index(n)))

                self.bookroom.remove(n)


class Person(Hotel):
    def guests(self):
        return print('This class do not have method guests!')

    def __str__(self):
        return self.name + ' is rented ' + ','.join(self.rentroom) + \
               ' room(s), and he(she) is book ' + ','.join(self.bookroom) + \
               ' room(s).'


bob = Person('Bob Smith')
bob.rent_room('101', '102')
sam = Person('Sam Jhons')
sam.rent_room('103')
print(bob)
bob.check_out('102')
print(sam)
Hotel.guests()
