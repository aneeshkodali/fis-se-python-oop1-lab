#!/usr/bin/env python3

class Book:
    

    # init
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # page_count - getter
    def get_page_count(self):
        return self._page_count
    
    # page_count - setter
    def set_page_count(self, value):

        # ensure valid value
        if type(value) is int:
            self._page_count = value

        # otherwise print message indicating erroneous value
        else:
            print("page_count must be an integer")

    # page_count - property
    page_count = property(
        fget=get_page_count,
        fset=set_page_count
    )

    # page_count - turn page
    def turn_page(self):

        # increment page_count
        self.page_count += 1

        # print message
        print("Flipping the page...wow, you read fast!")
        
    
        