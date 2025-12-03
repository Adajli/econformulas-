# econformulas
This is a python project for basic economic calculations including opportunity cost, comparative advantage, and... This project provides easy-to-use classes to explore college level economic concepts programmatically.The package will gather all the tools and methods into a single library making it easier to quickly compute standard economic quantities.
## Functionality
The package can be used by professors to generate examples and demonstrations to be used during lectures.
Students studying principle economics courses may also use the package to check their understanding and improve their efficiency in tests.
We hope that this package will cut repetition and errors from algebraic calculations making it useful for professionals conducting basic economic calculations in their day to day.

## Installation 
Install the required packages using pip:

pip install numpy

## Classes
### 1.Opportunity Cost
Calculates opportunity cost and identifies alternative with comparative advantage.
#### Attributes:
*OC_A*: Opportunity cost of choosing A  

*OC_B*: Opportunity cost of choosing B  

*cost*: Calculated Opportunity cost  

*time_value*: Value of one hour of time  

*default_units* : Label for the cost units (dollars)

#### Methods:
*cost_of_time(hours)*: Calculates opportunity cost of the number of hours worked using the attribute *time_value*. 

*compare_alternatives(value_A, value_B)*: Returns opportunity costs of both options.  

*comparative_advantage(time_A,time_B)*: Checks opportunity cost and returns which alternative has the lower opportunity cost.

#### Usage:
```
from econformulas import OpportunityCost
  oc = OpportunityCost(time_A=10, time_B=5)
  oc.show_comparison(10, 5)
  print("Comparative Advantage:", oc.comparative_advantage())
```  
### 2.DemandSupplyShifts
Calculate elasticity and predict changes in demand and supply of quantity based on change in price
#### Attributes:
*elasticity_d*: Demand elasticity

*elasticity_s*: Supply elasticity

#### Methods:
*calculate_elasticity(percent_change_quantity, percent_change_price)*: Computes elasticity.

*predict_quantity_change(percent_change_price, elasticity, market)*: Predicts % change in quantity.

*classify_elasticity(elasticity_value)*: Identifies type of elasticity provided.

#### Usage:
```from econformulas import DemandSupplyShifts

ds = DemandSupplyShifts(elasticity_d=1.5, elasticity_s=0.8)
elasticity = ds.calculate_elasticity([10, 15], [5, 10])
print("Elasticity:", elasticity)

quantity_change = ds.predict_quantity_change([5, 10], 1.5)
print("Predicted Quantity Change:", quantity_change)

income_effect = ds.shift_due_to_income(10, 0.2)
print("Shift due to income:", income_effect)
```
#### License
This project is open-source and free to use under the MIT License
