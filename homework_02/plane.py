"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: float = 0
    max_cargo: float = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload
        self.cargo += weight

    def remove_all_cargo(self):
        return_value, self.cargo = self.cargo, 0
        return return_value
