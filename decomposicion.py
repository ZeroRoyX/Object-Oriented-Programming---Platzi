class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self._status = 'Park'
        self._engine = Engine(cylinders = 4)

    def accelerate(self, speed = 'slow'):
        if speed == 'fast':
            self._engine_inject_gas(10)
        else:
            self._engine_inject_gas(3)

        self._status = 'Drive'
    
    def gas_light(self, level)
        if level <= 15%:
            self._turn_on_fuel_low()


class Engine:
    def __init__(self, cylinders, type = 'IC Engine'):
        self.cylinders = cylinders
        self.type = type
        self.temperature = 0
        
    def _fuel_injection(self, qty):
        pass

if __name__ == '__main__':
    pass