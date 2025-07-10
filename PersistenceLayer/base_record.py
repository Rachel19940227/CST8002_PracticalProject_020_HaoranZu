"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLay
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

from abc import ABC, abstractmethod

class BaseRecord(ABC):
    """
    Abstract base class for emission records.
    Provides a contract for display method.
    """

    @abstractmethod
    def display(self):
        """
        Display the content of the record in a specific format.
        Must be overridden in subclasses.
        """
        pass
    