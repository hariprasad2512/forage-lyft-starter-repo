from abc import ABC
from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable,ABC):
    def __init__(self, last_service_date):
        self.__engine = Engine()
        self.__battery = Battery()
        self.last_service_date = last_service_date

    def needs_service(self):
        return super().needs_service()
