class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the CashRegister with a total of 0, a discount (default is 0),
        an empty list of items, and a last_transaction amount of 0.
        """
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        :param item: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item (default is 1).
        """
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        """
        Apply the discount to the total.
        :return: A message indicating the new total after the discount or a message
                 stating there is no discount to apply.
        """
        if self.discount > 0:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
            return f"After the discount, the total comes to ${self.total}."
        else:
            print("There is no discount to apply.")
            return "There is no discount to apply."

    def void_last_transaction(self):
        """
        Void the last transaction by subtracting its amount from the total.
        If there are no items, reset the total to 0.0.
        """
        if self.items:
            self.total -= self.last_transaction
            self.last_transaction = 0
        else:
            self.total = 0.0