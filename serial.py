"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start_num=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start_num):
        self.start_num = start_num
        self.next_num = start_num - 1

    def generate(self):
        self.next_num = self.next_num + 1
        return self.next_num

    def reset(self):
        self.next_num = self.start_num - 1
        return self.start_num
