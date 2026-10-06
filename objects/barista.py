class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return(str(self.name + ": " + str(self.price)))

class Order:
    def __init__(self, receipt):
        self.receipt = receipt
    
    def add_item(self, item):
        self.receipt.append(item)        
    
    def calculate_taxes(self):
        tax = 0
        for item in self.receipt:
            tax += item.price * 0.07

    def __str__(self):
        for item in self.receipt:
            return(str(item))
def main():
   
    menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
    
    order1 = Order([])
    order1.add_item(menu[1])
    print(order1)

if __name__ == '__main__':
	main()
