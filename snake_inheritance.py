class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.num_ears = 2
    def breath(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        self.name = "bebo"
        print(f"{self.name} nemo swim")

    def breath(self):
        super().breath()
        print("I am under water.")




nemo = Fish()

nemo.breath()



