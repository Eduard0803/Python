class Person:
    def __init__(self, name:str=None, age:int=None, phone_number:str=None) -> None:
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def get_name(self) -> str:
        return self.name
    def get_age(self) -> int:
        return self.age
    def get_phone_number(self) -> str:
        return self.phone_number
