class Person:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    def __str__(self):
        return f"{self.first_name}; {self.last_name}; {self.address}"