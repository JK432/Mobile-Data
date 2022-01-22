# Define a class Mobile to store the details of a mobile (company, model, and price) with the following methods
# 1. set_details() --> to set the values to the data attributes
# 2. display_details()--> to display the data attribute values
# Create an object of class and invoke the methods   
class Mobile:
  def set_details(self):
    self.company=input()
    self.model=input()
    self.price=input()

  def display_details(self):
    print("\nDetails:-") 
    print("Company:",self.company)
    print("Model:",self.model)
    print("Price:",self.price)

M1=Mobile()
M1.set_details()
M1.display_details()