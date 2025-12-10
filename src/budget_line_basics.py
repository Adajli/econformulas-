class BudgetLinebasics:
    def __init__(self, priceX,priceY):
        # Defines the price as part of your budget for good X
        self.priceX = priceX
        # Defines the price as part of your budget for good Y
        self.priceY = priceY
        if not isinstance(priceX,(int,float) or not isinstance(priceY,(int,float))):
            raise TypeError("Please insert a numerical value")
        
    def calculateIncome(self,MU_X,MU_Y):
        '''
        The income is determined using the MU of goods X and Y.
        :param self: Description
        :param MU_X: Marginal Utility of good X
        :param MU_Y:  Marginal Utility of good Y
        '''
        if not isinstance(MU_X,(int,float) or not isinstance(MU_Y,(int,float))):
            raise TypeError("Please insert a numerical value")
        income = MU_X*self.priceX+MU_Y*self.priceY
        return income
    
    def printIncome(self,X,Y):
        '''
        Prints the calculated with these paremeters
        :param self
        :param X: The X used as the price.
        :param Y: The Y used for the price.
        '''
        print(self.calculateIncome(X,Y))

    def checkBudget(self,cost,X,Y):
        '''
        Checks whether or not you can spend an item with your income at a specific cost with these 
        paremeters
        :param cost: Cost determines whether or not you can spend an item with your income.
        :param X: The amount of X to determine overall cost for X items.
        :param Y: The amount of Y to determine overall cost for Y items.
        '''
        Income = self.calculateIncome(X,Y)
        if cost <= Income:
            print("You can spend the item with your income.")
        else:
            print("You can not spend the money with your income.")
    
    def printBudgetline(self):
        '''
        Prints out budget
        '''
        print(f"Budget line:{self.priceX}X+{self.priceY}Y= Income")
    
    def calculateBangPerBuck(self,MU):
        '''
        Calculates the bang per buck using MU attribute to insert with MU/priceX = MU/priceY with 
        these attributes
        :param MU: Sets up Marginal Utility to determine what good to choose or if it is optimal.

        '''
        bpbX = MU/self.priceX
        bpbY = MU/self.priceY
        if not isinstance(MU,(int,float)):
            raise TypeError("Please insert a numerical value")
        if self.priceY <= 0 or self.priceX <= 0:
            raise ValueError("The price must be non zero ")
        
        if bpbX>bpbY:
            print("Choose more of good X (higher bang per buck ratio)")
        elif bpbX<bpbY:
            print("Choose more of good Y (higher bang per buck ratio)")
        else:
            print("This is the optimal consumer bundle")

        
budget = BudgetLinebasics(20,20) # Set up for a budget line.
budget.calculateIncome(10,10) # Calculates income, which results in 400
budget.printIncome(10,10) #Prints income as a result
budget.printBudgetline() # Prints Budget line: 20X + 20Y = Income
budget.calculateBangPerBuck(10) # Prints "This is the optimal consumer bundle"
budget.checkBudget(600,10,10) # Prints "You can not spend the money on your income"