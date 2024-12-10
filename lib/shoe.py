#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand ,size):
        self._brand = brand
        self._size = size
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"
    
    @property
    def brand (self):
        return self._brand
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            print('size must be an integer')
        self._size = value
    @brand.setter
    def brand(self,value):
        if not isinstance(value,str):
            print('brand must be a string')
        self._brand = value
    
    @property
    def condition(self):
        return self._condition