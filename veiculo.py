opt = int(input("1 - Carro \n2 - Bicicleta \n3 - Moto \nDigite uma das opções acima: "))

match opt:
    case 1:
        class Vehicle:
            def __init__(self):
                self.name = str(input("Digite o nome do veículo: "))
                self.color = str(input("Digite a cor do veículo: "))
                self.model = str(input("Digite o modelo do veículo: "))

        class Car(Vehicle):
            def __init__(self):
                super().__init__()

            def info(self):
                return f"O seu veículo é um {self.name}, a cor do {self.name} é {self.color} e o modelo dele é {self.model}"
        
        car = Car()
        print(car.info())

    case 2:
        class Vehicle:
            def __init__(self):
                self.name = str(input("Digite o nome do veículo: "))
                self.color = str(input("Digite a cor do veículo: "))
                self.model = str(input("Digite o modelo do veículo: "))

        class Bike(Vehicle):
            def __init__(self):
                super().__init__()
            
            def info(self):
                return f"O seu veículo é um {self.name}, a cor do {self.name} é {self.color} e o modelo dele é {self.model}"
            
        bike = Bike()
        print(bike.info())

    case 3:
        class Vehicle:
            def __init__(self):
                self.name = str(input("Digite o nome do veículo: "))
                self.color = str(input("Digite a cor do veículo: "))
                self.model = str(input("Digite o modelo do veículo: "))

        class Motorbike(Vehicle):
            def __init__(self):
                super().__init__()
            
            def info(self):
                return f"O seu veículo é um {self.name}, a cor do {self.name} é {self.color} e o modelo dele é {self.model}"

        moto = Motorbike()
        print(moto.info())