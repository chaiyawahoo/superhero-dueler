class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
    
    def bark(self):
        return "Woof!"
    
    def sit(self):
        return f"{self._name} sits."
    
    def rollover(self):
        return f"{self._name} rolls over."
