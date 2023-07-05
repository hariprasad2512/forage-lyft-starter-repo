from abc import ABC
from engine import Engine


class CapuletEngine(Engine,ABC):
    __current_mileage = None
    __last_service_mileage = None
    def __init__(self,last_service_mileage,current_mileage):
    
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        return super().needs_service()
    
    