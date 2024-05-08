from abc import ABC, abstractmethod
from config import config

class evaluation_chain:
    def __init__(self):
        self.steps = []

    def add_evaluation_step(self, step):
        self.steps.append(step)

    def execute(self):
        for step in self.steps:
            step.execute()

class evaluation_step(ABC):
    _config: config

    def __init__(self, _config: config):
        self._config = _config

    @abstractmethod
    def execute(self):
        """Handle the config."""
        pass