class Washing_machine:
    def __init__(self):
        pass

    def wash(self, temperature = 'cold'):
        """Método público que se llama 'wash' y recibe una temperatura e 
        internamente el método llamará a varios métodos privados, cosas
        que el usuario no le interesaría cómo funciona.
        """   
        self._water_fill(temperature)
        self._add_soap()
        self._wash()
        self._centrifugate()

    def _water_fill(self, temperature):
        print(f'Filling with {temperature} water.')

    def _add_soap(self):
        print(f'Adding soap...')
    
    def _wash(self):
        print(f'Washing...')
    
    def _centrifugate(self):
        print(f'Spinning...')


if __name__ == '__main__':
    
    washing_machine = Washing_machine()
    washing_machine.wash('warm')