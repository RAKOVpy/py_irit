class Transport:
    """
    coordinates, speed, brand, year, number
    """

    def __init__(self, *args, **kwargs):
        d_vals_array = ['coordinates', 'speed', 'brand', 'year', 'number']
        d_vals = {str(i): None for i in d_vals_array}

        if len(args) + len(kwargs) != 5:
            raise Exception('Wrong quantity of аrguments')

        for i in kwargs:
            if i in d_vals:
                d_vals[i] = kwargs[i]

        index = 0
        for j in d_vals_array:
            if d_vals[j] is None:
                d_vals[j] = args[index]
                index += 1

        self.__coordinates = d_vals['coordinates']
        self.__speed = d_vals['speed']
        self.__brand = d_vals['brand']
        self.__year = d_vals['year']
        self.__number = d_vals['number']

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def __str__(self):
        """
        Представление всей информации для вывода в методе print()
        """
        line_print = ''
        d = self.__dict__
        for i in d:
            line_print += f'{i}: {d[i]}\n'
        return line_print

    def is_in_area(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        if not (pos_x <= self.coordinates[0] <= pos_x + width):
            return False
        if not (pos_y - length <= self.coordinates[1] <= pos_y):
            return False
        return True


class Passenger:
    def __init__(self, number_of_passengers=None, passengers_capacity=None):
        self.__number_of_passengers = number_of_passengers
        self.__passengers_capacity = passengers_capacity

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    """
    coordinates, speed, brand, year, number, height
    """

    def __init__(self, *args, **kwargs):
        if 'height' in kwargs:
            self.__height = kwargs['height']
            del kwargs['height']
            super().__init__(*args, **kwargs)
        else:
            self.__height = args[-1]
            super().__init__(*args[:-1], **kwargs)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Auto(Transport):
    """
    coordinates, speed, brand, year, number
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ship(Transport):
    """
    coordinates, speed, brand, year, number, port
    """

    def __init__(self, *args, **kwargs):
        if 'port' in kwargs:
            self.__port = kwargs['port']
            del kwargs['port']
            super().__init__(*args, **kwargs)
        else:
            self.__port = args[-1]
            super().__init__(*args[:-1], **kwargs)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port


class Car(Auto):
    """
    coordinates, speed, brand, year, number
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bus(Auto, Passenger):
    """
    coordinates, speed, brand, year, number, number_of_passengers, passengers_capacity
    """

    def __init__(self, *args, **kwargs):
        if 'passengers_capacity' in kwargs:
            self.passengers_capacity = kwargs['passengers_capacity']
            del kwargs['passengers_capacity']
        else:
            self.passengers_capacity = args[-1]
            args = args[:-1]

        if 'number_of_passengers' in kwargs:
            self.number_of_passengers = kwargs['number_of_passengers']
            del kwargs['number_of_passengers']
        else:
            self.number_of_passengers = args[-1]
            args = args[:-1]

        super().__init__(*args, **kwargs)


class CargoAuto(Auto, Cargo):
    """
    coordinates, speed, brand, year, number, carrying
    """

    def __init__(self, *args, **kwargs):
        if 'carrying' in kwargs:
            self.carrying = kwargs['carrying']
            del kwargs['carrying']
        else:
            self.carrying = args[-1]
            args = args[:-1]

        super().__init__(*args, **kwargs)


class Boat(Ship):
    """
    coordinates, speed, brand, year, number, port
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    """
    coordinates, speed, brand, year, number, port, number_of_passengers, passengers_capacity
    """

    def __init__(self, *args, **kwargs):
        if 'passengers_capacity' in kwargs:
            self.passengers_capacity = kwargs['passengers_capacity']
            del kwargs['passengers_capacity']
        else:
            self.passengers_capacity = args[-1]
            args = args[:-1]

        if 'number_of_passengers' in kwargs:
            self.number_of_passengers = kwargs['number_of_passengers']
            del kwargs['number_of_passengers']
        else:
            self.number_of_passengers = args[-1]
            args = args[:-1]

        super().__init__(*args, **kwargs)


class CargoShip(Ship, Cargo):
    """
    coordinates, speed, brand, year, number, port, carrying
    """

    def __init__(self, *args, **kwargs):
        if 'carrying' in kwargs:
            self.carrying = kwargs['carrying']
            del kwargs['carrying']
        else:
            self.carrying = args[-1]
            args = args[:-1]

        super().__init__(*args, **kwargs)


class SeaPlane(Plane, Ship):
    """
    coordinates, speed, brand, year, number, port, height
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


t = SeaPlane([10, 20], 'toi', '13-52-64', 'ai', 1000, year=1991, speed=10)
print(t)
