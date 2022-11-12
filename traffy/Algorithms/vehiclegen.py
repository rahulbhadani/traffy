#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2022-11-12
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
# For System and OS level task
import sys, getopt
from abc import ABC, abstractmethod

class vehiclgen(ABC):
    """
    Abstract Vehicle Generator Class

    """

    def __init__(self, sim, config={}, *args, **kwargs):
        self.sim = sim

        # Set default configurations
        self.set_default_config()

        # Update configurations
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
    def generate_vehicle(self):
        pass

    @abstractmethod
    def update(self):
        pass