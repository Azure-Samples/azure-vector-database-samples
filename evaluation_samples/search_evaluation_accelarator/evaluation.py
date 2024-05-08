from abc import ABC, abstractmethod

class evaluation_chain:
    def __init__(self):
        self.steps = []

    def add_evaluation_step(self, step):
        self.steps.append(step)

    def execute(self):
        for step in self.steps:
            step.execute()

class evaluation_step(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def execute(self):
        """Handle the config."""
        pass