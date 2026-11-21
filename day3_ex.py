class mini_calculator:
    def __init__(self, numbers_list, input_number, operation):
        self.numbers_list = numbers_list
        self.input_number = input_number
        self.operation = operation
        

    def verification(self, numbers_list, input_number):
        if input_number not in numbers_list:
            print(f"Le nombre {input_number} n'existe pas dans la liste")
        else:
            print(f"Le nombre {input_number} existe dans la liste")


    def to_string(self):
        return str(self.input_number)

    def to_float(self):
        return float(self.input_number)

    def to_square(self):
        self.input_number = self.input_number ** 0.5

    def indice(self):
        self.input_number = self.numbers_list.index(self.input_number)


    def type_interlopation(self, input_number):
        print("---Type Interlopation---")
        # verification du type
        print(f'type du nombre entrer, {type(input_number)}')
        print(f'type du list, {type(self.numbers_list)}')
        print(f'type float input, {type(self.to_float())}')
        print(f'type string_number, {type(self.to_string())}')
        print(f'type square_input_number, {type(self.input_number)}')

    def calculer(self, numbers_list.index(input_number)):
        match self.operation:
            case "+":
                return f"sum = {self.input_number + index}"
            case "-":
                return f"sub = {self.input_number - index}"
            case "*":
                return f"multiply = {self.input_number * index}"
            case "/":
                if index != 0:
                    return f"div = {self.input_number / index}"
                else:
                    print("Division par zéro")
            case "//":
                return f"div = {self.input_number // index}"
            case "%":
                return f"modulo = {self.input_number % index}"
            case _:
                print("Opération non prise en compte")
                return None


calculer1 = mini_calculator([1, 2, 3, 7], 3, '*');
print(calculer1.calculer(0))