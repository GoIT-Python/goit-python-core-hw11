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
        data_list = list(self.data)[:n]
        for key in data_list:
            print(key, self.data.get(key))


book = AddressBook()
book['a'] = 'Anna'
book['b'] = 'Boris'
book['c'] = 'Doris'
book['d'] = 'Gloria'
book['e'] = 'Joan'

if __name__ == '__main__':
    book.iterator(3)
