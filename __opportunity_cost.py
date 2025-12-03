import numpy as np
class OpportunityCost:
    def __init__(self, time_value=None, default_units="dollars"):
    # time_value : value of one hour of time (float)
    # default_units : label for the cost units (str) 
        self.time_value = time_value
        self.default_units = default_units
    def cost_of_time(self,hours):
    # Calculates opportunity cost of hours spent
        self.cost = np.array(hours) * self.time_value
        return self.cost
    def compare_alternatives(self, value_A, value_B):
    #Compares opportunity costs of two alternatives
    #value_A: the benefit/value you get from choosing A
    #value_B: the benefit/value you get from choosing B

    #Returns:
    #   choose_A_cost = what you give up (value of B)
    #   choose_B_cost = what you give up (value of A) 
        self.cost_of_A = value_B
        self.cost_of_B = value_A
        return self.cost_of_A,self.cost_of_B
    
    def comparative_advantage(self, time_A, time_B):
    #Compares comparative advantage of two values
    #Lower opportunity cost = comparative advantage
        #calculates opportunity cost
        self.OC_A = time_A/time_B
        self.OC_B = time_B/time_A 
        #checks for comparative advantage
        if self.OC_A < self.OC_B:
            return f"A has comparative advantage (OC={self.OC_A:.3f})"
        elif self.OC_B < self.OC_A:
            return f"B has comparative advantage (OC={self.OC_B:.3f})"
        else:
            return "Neither has a comparative advantage (opportunity costs are equal)"
        
opp_cost = OpportunityCost(45)
opp_cost.cost_of_time(5)
print(opp_cost.cost)
opp_cost.compare_alternatives(10,14)
print(opp_cost.cost_of_A,opp_cost.cost_of_B)
print(opp_cost.comparative_advantage(5,8))


