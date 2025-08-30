class myCar:      
    def __init__(self, make, model, year):  
        self.make = make  
        self.model = model  
        self.year = year  
        
    def drive(self):
        print (f"He is driving a {self.make} {self.model} model {self.year}.")

myCar1 = myCar('Toyota', 'Corolla', 2020)
myCar2 = myCar('Honda', 'Civic', 2019) 
myCar1.drive()
myCar2.drive()  

    