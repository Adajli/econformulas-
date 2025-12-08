from ..budget_line_basics import BudgetLinebasics

def test_Income():
    budget = BudgetLinebasics(20,20)
    output = budget.calculateIncome(10,10)
    assert output > 0
test_Income()