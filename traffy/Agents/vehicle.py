#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2022-11-12
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
# For System and OS level task
import sys, getopt
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract vehicle class to implement specific vehicle types such as intelligent driver models

    """
    def __init__(self, config={},  *args, **kwargs):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    @abstractmethod
    def set_default_config(self):    
        pass

    @abstractmethod
    def init_properties(self):
        pass

    @abstractmethod
    def update(self, lead, dt):
        pass

    @abstractmethod
    def stop(self):
        pass

    def unstop(self):
        pass

    def slow(self, v):
        pass

    def unslow(self):
        pass
        
