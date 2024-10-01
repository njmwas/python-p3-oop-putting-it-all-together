#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count) -> None:
        self.title = title
        self.page_count = page_count
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, count):
        if not isinstance(count, int):
            print("page_count must be an integer")
        else:
            self._page_count = count
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        