class BudgetLinebasics:
    def __init__(self, priceX,priceY,MU_X,MU_Y):
        self.priceX = priceX
        self.priceY = priceY
        self.MU_X = MU_X
        self.MU_Y = MU_Y

    def checkBudget(self, priceX,priceY,Income,MU_X,MU_Y):
        if(priceX*MU_X+priceY*MU_Y <= Income):
            print("You can spend the item with this income.")
        else:
            print("You can not spend the money on your income.")
