#!/usr/bin/env python3

class Coffee:
    
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # size - getter
    def get_size(self):
        return self._size
    
    # size - setter
    def set_size(self, value):

        # ensure valid value
        if value in ('Small', 'Medium', 'Large'):
            self._size = value
        
        # otherwise print message indicating erroneous value
        else:
            print("size must be Small, Medium, or Large")

    # size - property
    size = property(
        fget=get_size,
        fset=set_size
    )

    # price - tip
    def tip(self):

        # print message
        print("This coffee is great, here’s a tip!")

        # increment price
        self.price += 1