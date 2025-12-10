import numpy as np
from opoortunitycost import OpportunityCost

def test_cost_of_time():
    model = OpportunityCost(15)
    output = model.cost_of_time(5)
    assert output == 75 #15*5 = 75

def test_compare_alternatives():
    model = OpportunityCost(15)
    output = model.compare_alternatives(10,5)
    assert output == (5,10) 

def  test_comparative_advantage():
    model = OpportunityCost(15)
    output = model.comparative_advantage(5,10)
    assert output == "A has comparative advantage (OC=0.500)"