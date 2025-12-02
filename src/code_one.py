class BudgetLinebasics:
    def __init__(self, priceX,priceY):
        self.priceX = priceX
        self.priceY = priceY

    def checkBudget(self, priceX,priceY,Income,X,Y):
        if(priceX*X+priceY*Y <= Income):
            print("You can spend the item with this income.")
        else:
            print("You can not spend the money on your income.")
