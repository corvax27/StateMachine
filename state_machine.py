from abc import ABCMeta, abstractmethod


class AbstractState(metaclass=ABCMeta):
    def __init__(self):
        self.__next_state = None

    @abstractmethod
    def execute(self):
        pass

    @property
    def next_state(self):
        return self.__next_state

    @next_state.setter
    def next_state(self, value):
        self.__next_state = value


class StateMachine:
    def __init__(self, initial_state: AbstractState):
        self.current_state = initial_state

    def execute(self):
        self.current_state.execute()

    def transition(self):
        self.current_state = self.current_state.next_state

    def has_state(self):
        return self.current_state is not None
