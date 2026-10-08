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
        return tax
    
    def calculate_total(self):
        total = 0
        for item in self.receipt:
            total += item.price * 1.07
        return total
    
    def print_receipt(self):
            print("fun with objects cafe")
            print("---------------")
            print(self.__str__())
            print("---------------")
            print("Tax:")
            print("$" + str(self.calculate_taxes()))
            print("---------------")
            print("Total:")
            print("$" + str(self.calculate_total()))

    def __str__(self):
        x = ""
        for item in self.receipt:
            x += str(item)
            x += " "
        return(x)
            
    

def main():
   
    menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
    
    order1 = Order([])
    order1.add_item(menu[1])
    order1.add_item(menu[1])
    order1.add_item(menu[2])
    total = order1.calculate_total()
    print("The total due is $" + str(total))
    order1.print_receipt()

if __name__ == '__main__':
	main()
