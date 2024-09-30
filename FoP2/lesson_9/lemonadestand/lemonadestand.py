from menu_item import MenuItem
from sales_for_day import SalesForDay

class InvalidSalesItemError(Exception):
    pass

class LemonadeStand:
    def __init__(self, stand_name) -> None:
        self._stand_name = stand_name
        self._current_day = 0
        self._menu_dict = {} # {item_name: MenuItem obj}
        self._sales_record_lst = [] #[SalesForDay obj]

    def __str__(self):
        print(f"{self._stand_name}, {self._current_day}, {self._menu_dict}, {self._sales_record_lst}")

    def get_name(self):
        return self._stand_name
    
    def add_menu_item(self, menu_item_obj):
        self._menu_dict[menu_item_obj.get_name()] = menu_item_obj
    #   print(self._menu_dict[menu_item_obj.get_name()])
    def enter_sales_for_today(self, sold_items_dict):         
        for item in sold_items_dict:
            if item in self._menu_dict:
                new_sales_record_obj = SalesForDay(self._current_day, sold_items_dict)
                self._sales_record_lst.append(new_sales_record_obj)
                self._current_day += 1
            else:
                raise InvalidSalesItemError(f"{item} is not in the menu.")

    def sales_of_menu_item_for_day(self, day_of_sale, item_name):
        for sale in self._sales_record_lst:
            sale_obj = self._sales_record_lst[day_of_sale].get_sales_dict()
            if sale_obj[item_name]:
                return sale_obj[item_name]
            else:
                return 0
        return 'Menu item was not found'
    
    def total_sales_for_menu_item(self, item_name):
        total = 0
        for i, sale in enumerate(self._sales_record_lst):
            total += self.sales_of_menu_item_for_day(i, item_name)
        return total
    
    def total_profit_for_menu_item(self, item_name):
        total_sales = self.total_sales_for_menu_item(item_name)
        gross_revenue = 0
        gross_expense = 0
        profit_of_item = gross_revenue - gross_expense
        for i, sale in enumerate(self._sales_record_lst):
            menu_obj = self._menu_dict[item_name]
            gross_revenue += total_sales * menu_obj.get_selling_price()
            gross_expense += total_sales * menu_obj.get_wholesale_cost()
        profit_of_item = gross_revenue - gross_expense 
        # print(profit_of_item)
        return profit_of_item

    def total_profit_for_stand(self):
        total_stand_profit = 0
        for i, sale in enumerate(self._sales_record_lst):
            menu_obj_name = self._sales_record_lst[i].get_sales_dict()
            for name in menu_obj_name.keys():
                total_stand_profit += self.total_profit_for_menu_item(name)               
        # print(total_stand_profit, 'here')
        return total_stand_profit


stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

# This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
day_0_sales = {
    'lemonade' : 5,
    'cookie'   : 2
}

stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero

stand.sales_of_menu_item_for_day(0, 'lemonade')
print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far

stand.total_profit_for_stand()