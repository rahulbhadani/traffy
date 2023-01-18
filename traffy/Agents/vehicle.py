#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2022-11-12
# The author's name and email are stored in these variables
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
# Importing the sys and getopt modules for system and OS level tasks
import sys, getopt
# Importing the ABC (Abstract Base Class) module to define an abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract vehicle class to implement specific vehicle types such as intelligent driver models

    """
    def __init__(self, config={},  *args, **kwargs):
        """
        The constructor method for the class. It sets the default configuration for the vehicle
        and updates it with any configuration passed in as an argument. It also calls the 
        init_properties method to calculate the properties of the vehicle.
        """
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    @abstractmethod
    def set_default_config(self):    
        """
        Abstract method that must be implemented by subclasses. It sets the default configuration
        for the vehicle.
        """
        pass

    @abstractmethod
    def init_properties(self):
        """
        Abstract method that must be implemented by subclasses. It calculates the properties of 
        the vehicle.
        """
        pass

    @abstractmethod
    def update(self, lead, dt):
        """
        Abstract method that must be implemented by subclasses. It updates the vehicle's state 
        based on the state of the lead vehicle and the time step dt.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Abstract method that must be implemented by subclasses. It stops the vehicle.
        """
        pass

    def unstop(self):
        """
        Method that un-stops the vehicle.
        """
        pass

    def slow(self, v):
        """
        Method that slows down the vehicle to the specified velocity v.
        """
        pass

    def unslow(self):
        """
        Method that un-slows the vehicle.
        """
        pass
