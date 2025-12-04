#import pytest
import numpy as np
from demandsupplyshifts import DemandSupplyShifts
def test_calculate_elasticity_correct_output():
    model = DemandSupplyShifts()
    result = model.calculate_elasticity(8, 2)
    assert result == 4     # 8/2 = 4

def test_calculate_elasticity_array_inputs():
    model = DemandSupplyShifts()
    pcq = np.array([10, 20])
    pcp = np.array([5, 10])
    result = model.calculate_elasticity(pcq, pcp)
    np.testing.assert_array_equal(result, np.array([2.0, 2.0]))

def test_predict_quantity_uses_supply_elasticity():
    model = DemandSupplyShifts(elasticity_d=3, elasticity_s=2)
    result = model.predict_quantity_change(5, market="supply")
    assert result == 10   # 2 * 5

def test_predict_quantity_passed_elasticity_argument():
    model = DemandSupplyShifts()
    result = model.predict_quantity_change(5, elasticity=0.5)
    assert result == 2.5   # 0.5 * 5

def test_classify_elasticity_elastic():
    model = DemandSupplyShifts()
    assert model.classify_elasticity(2.5) == "elastic"

def test_classify_elasticity_unit_elastic():
    model = DemandSupplyShifts()
    assert model.classify_elasticity(1.0) == "unit elastic"