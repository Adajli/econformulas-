class BudgetLinebasics:
    def __init__(self, priceX,priceY):
        self.priceX = priceX
        self.priceY = priceY
        if not isinstance(priceX,(int,float) or not isinstance(priceY,(int,float))):
            raise TypeError("Please insert a numerical value")
        
    def calculateIncome(self,MU_X,MU_Y):
        income = MU_X*self.priceX+MU_Y*self.priceY
        return income
    def printIncome(self,X,Y):
        print(self.calculateIncome(X,Y))
    def checkBudget(self,cost,X,Y):
        Income = self.calculateIncome(X,Y)
        if cost <= Income:
            print("You can spend the item with this income.")
        else:
            print("You can not spend the money on your income.")
    
    def printBudgetline(self):
        print(f"Budget line:{self.priceX}X+{self.priceY}Y= Income")
    
    def calculateBangPerBuck(self,MU):
        bpbX = MU/self.priceX
        bpbY = MU/self.priceY
        if self.priceY <= 0 or self.priceX <= 0:
            raise ValueError("The price must be non zero ")
        
        if bpbX>bpbY:
            print("Choose more of good X (higher bang per buck ratio)")
        elif bpbX<bpbY:
            print("Choose more of good Y (higher bang per buck ratio)")
        else:
            print("This is the optial bundle")

        
budget = BudgetLinebasics(20,20)
budget.calculateIncome(10,10)
budget.printIncome(10,10)
budget.printBudgetline()
budget.checkBudget(600,10,10)