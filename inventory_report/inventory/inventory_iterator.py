from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_index = 0

    def __next__(self):
        try:
            data = self.data[self.current_index]

            self.current_index += 1

            return data
        except IndexError:
            raise StopIteration
