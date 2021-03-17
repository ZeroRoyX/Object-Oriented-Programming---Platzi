class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        return 'Ando caminando.'
    
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        return 'ando pedaleando.'


def run():

    persona = Persona('Roy')
    ciclista = Ciclista('Ara')

    print(persona.avanza())
    print(ciclista.avanza())

if __name__ == '__main__':
    run()
