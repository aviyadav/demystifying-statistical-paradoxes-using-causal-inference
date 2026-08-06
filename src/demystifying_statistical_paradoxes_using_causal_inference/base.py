from abc import ABC, abstractmethod

class ParadoxExample(ABC):
    """Base class for statistical paradox examples."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the paradox."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """A brief description of the paradox and why it occurs."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Execute the paradox demonstration."""
        pass
