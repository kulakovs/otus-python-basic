from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: float = None
    started: bool = False
    fuel: float = None
    fuel_consumption: float = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel == 0:
                raise LowFuelError
            self.started = True

    def move(self, distance):
        diff = self.fuel - self.fuel_consumption * distance
        if diff < 0:
            raise NotEnoughFuel
        self.fuel = diff
