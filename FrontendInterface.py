from abc import ABC, abstractmethod

class FrontendInterface(ABC):
    @abstractmethod
    def run(self):
        pass
