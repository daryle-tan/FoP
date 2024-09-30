from menu_item import MenuItem

class SalesForDay:
    def __init__(self, days_opened, items_sold_dict) -> None:
        self._days_opened = days_opened
        self._items_sold_dict = items_sold_dict # {name of items sold: number of items sold that day}

    def __str__(self):
        return f"{self._days_opened} and {self._items_sold_dict}"
    
    def get_day(self):
        return self._days_opened
    
    def get_sales_dict(self):
        return self._items_sold_dict
    