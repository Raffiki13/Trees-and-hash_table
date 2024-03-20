class People:
    '''
    Класс информации о жителях и их месте проживания

    :param name: Полное ФИО
    :type name: str
    :param street: Название улицы проживания
    :type street: str
    :param building: Номер дома
    :type building: int
    :param flat: Номер квартиры
    :type flat: int
    :param date_of_birth: Дата рождения
    :type date_of_birth: str
    '''
    def __init__(self, name:str, street:str, building:int, flat:int, date_of_birth:str, data:str):
        '''
        Конструктор
        '''
        self.name = name
        self.street = street
        self.building = building
        self.flat = flat
        self.date_of_birth = date_of_birth
        self.data = data
    
    def __eq__(self, other):
        '''
        Пегрузка оператора равенства

        :param other: Объект класса People
        :type  other: People
        '''
        return (self.name == other.name and self.street == other.street and
            self.building == other.building and self.flat == other.flat and
            self.date_of_birth == other.date_of_birth)
    
    def __lt__(self, other):
        '''
        Пегрузка оператора меньше

        :param other: Объект класса People
        :type  other: People
        '''
        return ((self.street < other.street) or 
            (self.street == other.street and self.building < other.building) or
            (self.street == other.street and self.building == other.building and self.flat < other.flat) or
            (self.street == other.street and self.building == other.building and self.flat == other.flat and self.name < other.name) or
            (self.street == other.street and self.building == other.building and self.flat == other.flat and self.name == other.name and self.date_of_birth < other.date_of_birth))
    
    def __le__(self, other):
        '''
        Пегрузка оператора меньше или равно

        :param other: Объект класса People
        :type  other: People
        '''
        return (self < other or self == other)
    
    def __gt__(self, other):
        '''
        Пегрузка оператора больше

        :param other: Объект класса People
        :type  other: People
        '''
        return (not (self < other))
    
    def __ge__(self, other):
        '''
        Пегрузка оператора больше или равно
        
        :param other: Объект класса People
        :type  other: People
        '''
        return ((not (self < other)) or self == other)
    
    def __repr__(self):
        '''
        Итераторы
        '''
        return self.data