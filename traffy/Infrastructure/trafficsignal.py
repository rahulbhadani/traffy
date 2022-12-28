#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2022-11-12
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
# For System and OS level task
import sys, getopt
from abc import ABC, abstractmethod, abstractproperty

class TrafficSignal(ABC):
    """
    Abstract Traffic Signal Class

    """

    def __init__(self,  config={}, *args, **kwargs):
        pass

    @abstractmethod
    def set_default_config(self):
        pass

    @abstractmethod
    def init_properties(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractproperty
    def current_cycle(self):
        pass

    
