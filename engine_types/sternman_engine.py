from abc import ABC

from engine import Engine
from car import Car


class SternmanEngine(Engine,ABC):

    __warning_light_on = None
    def __init__(self, warning_light_is_on):
        self.__warning_light_on = warning_light_is_on

    
    def needs_service(self):
        return super().needs_service()
    
    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
