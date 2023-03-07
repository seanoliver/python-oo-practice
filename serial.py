class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

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

    def __init__(self, start):
        """Create a new instance of SerialGenerator"""

        self.start = self.next = start

    # __repr__ method

    def generate(self):
        """Increment self.next by 1 and return self.next - 1"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset self.next to the initial starting value"""

        self.next = self.start

