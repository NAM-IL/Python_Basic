class Parent:
    def __init__(self):
        self.__private_var = "부모 값"
        self._protected_var = "부모 값"
        self.public_var = "부모 값"
    
    def show_private_value(self):
        print(f"__private_var: {self.__private_var}")
            
    def show_protected_value(self):
        print(f"_protected_var: {self._protected_var}")

    def show_public_value(self):
        print(f"public_var: {self.public_var}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private_var = "자식 값"
        self._protected_var = "자식 값"
        self.public_var = "자식 값"

if __name__ == "__main__":
    c = Child()
    c.show_private_value()
    c.show_protected_value()
    c.show_public_value()
    print(f"c.__dict__: {c.__dict__}")