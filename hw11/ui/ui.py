from collections import UserDict


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
    def __init__(self, name, phone=None):
        if phone is None:
            phone = []
        self.name = name
        self.phone = phone

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
