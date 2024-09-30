class MenuItem:
    def __init__(self, item_name, wholesale_cost, selling_price) -> None:
        self._item_name = item_name #str
        self._wholesale_cost = wholesale_cost #float
        self._selling_price = selling_price #float

    def __str__(self):
        return f"{self._item_name}, {self._wholesale_cost}, {self._selling_price}"
    
    def get_name(self):
        return self._item_name
    
    def get_wholesale_cost(self):
        return self._wholesale_cost
    
    def get_selling_price(self):
        return self._selling_price