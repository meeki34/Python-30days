class Car:#init mean initialization
    def __init__(self,model,year,color,for_sale):#this an dunder method
        #self is object we are create
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        # self.price = price
        # self.mileage = mileage
        # self.owner = owner
        # self.warranty = warranty
        
        


# method are action which operation can perfrom

    def drive(self):
        print(f"the {self.color}{self.model} is driving")
        

    def sell(self):
        print(f"the {self.color}{self.model} is selling")
        
    def describe(self):
        print(f"the {self.color}{self.model} is {self.year} year old")