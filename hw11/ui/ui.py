from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.NUMBER_RECORDS = None
        self.value = 0

    def __next__(self):
        if self.value >= self.NUMBER_RECORDS:
            raise StopIteration
        self.value += 1
        return self.value

    def __iter__(self):
        return self

    def iterator(self, n):
        self.NUMBER_RECORDS = n
        if self.data:
            data_list = list(self.data)[:n]
            for key in data_list:
                print(key, self.data.get(key))
        else:
            print('No records found')

    def get_records(self):
        for key, value in self.data.items():
            print(key.name, value)

    def search_record(self, key):
        print(self.data.get(key))
        return self.data

    def add_record(self, record):
        self.data[record.name] = record.phone


class Record:
    def __init__(self, name, phone=None, birthday=None):
        if phone is None:
            phone = []
        if birthday is None:
            bd = ''
        self.name = name
        self.phone = phone
        self.bd = birthday

    def add_phone(self, item):
        if item not in self.phone:
            self.phone.append(item)
        else:
            print(f"Phone number {item} already in list")

    def remove_phone(self, item):
        if item in self.phone:
            self.phone.remove(item)
        else:
            print(f"Phone number {item} is not in list")

    def edit_phone(self, item):
        self.phone.clear()
        self.phone.append(item)

    def days_to_birthday(self):
        now = datetime.now()
        ts_now = now.timestamp()
        one_year_interval = timedelta(weeks=52)
        birthday = datetime.strptime(self.bd.birthday, '%d-%m-%Y').date()
        ts_bd_0 = datetime(year=now.year, month=birthday.month, day=birthday.day).timestamp()
        delta = (ts_bd_0 - ts_now) // (24 * 3600) + 1
        if delta > 0:
            print(int(delta))
        elif delta < 0:
            print(int(delta + one_year_interval.days + 1))
        else:
            print('Say Happy Birthday to contact today!')


class Field:
    def __init__(self):
        pass


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self, phone=""):
        super().__init__()
        self.phone = phone

    def __str__(self):
        return self.phone


class Birthday(Field):
    def __init__(self, birthday):
        super().__init__()
        self.birthday = birthday

    def __str__(self):
        return self.birthday


record = Record('Boris')
record.bd = Birthday('23-05-1980')
record.days_to_birthday()
