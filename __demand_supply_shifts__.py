import numpy as np

class DemandSupplyShifts:
    def __init__(self, elasticity_d=None, elasticity_s=None):
        # demand elasticity
        self.elasticity_d = elasticity_d  
        # supply elasticity
        self.elasticity_s = elasticity_s 

        if elasticity_d is not None and (not isinstance(elasticity_d, (int, float)) or np.isnan(elasticity_d)):
            raise ValueError("elasticity_d must be a numeric value.")
        if elasticity_s is not None and (not isinstance(elasticity_s, (int, float)) or np.isnan(elasticity_s)):
            raise ValueError("elasticity_s must be a numeric value.")
    def calculate_elasticity(self, percent_change_quantity, percent_change_price):
        """
        Elasticity = %ΔQ / %ΔP
        Values as raed from graph
        """
        pcq = np.array(percent_change_quantity)
        pcp = np.array(percent_change_price)

        
        if np.any(pcp == 0):
            raise ValueError("Percent change in price cannot be zero")
        if np.any(np.isnan(pcq)) or np.any(np.isnan(pcp)):
            raise ValueError("Percent changes must be numeric and not NaN")

        return pcq / pcp
    def predict_quantity_change(self, percent_change_price, elasticity=None, market="demand"):
        """
        Predict %ΔQ using elasticity × %ΔP
        User may pass elasticity directly OR rely on stored elasticity
        """
        price_change = np.array(percent_change_price)

        # If elasticity not passed, use stored elasticity
        if elasticity is None:
            if market == "demand":
                elasticity = self.elasticity_d
            elif market == "supply":
                elasticity = self.elasticity_s
            else:
                raise ValueError("market must be 'demand' or 'supply'")

        if elasticity is None:
            raise ValueError("Elasticity must be provided or set in the class")
        if np.any(np.isnan(percent_change_price)):
            raise ValueError("Percent change in price must be numeric and not NaN")
        return elasticity * price_change
    
    def classify_elasticity(self, elasticity_value):
        e = float(elasticity_value)
        if e > 1:
            return "elastic"
        elif e == 1:
            return "unit elastic"
        else:
            return "inelastic"

model = DemandSupplyShifts(elasticity_d= 5,elasticity_s= 'three')  
elasticity = model.calculate_elasticity(8,2) 
print("Calculated elasticity:", elasticity)
prediction_demand = model.predict_quantity_change(3.6, market="demand")
print("Predicted %ΔQ (demand):", prediction_demand)
prediction_supply = model.predict_quantity_change(5.2, market="supply")
print("Predicted %ΔQ (supply):", prediction_supply)
elasticity_type = model.classify_elasticity(elasticity)
print(f" {elasticity} is {elasticity_type}")