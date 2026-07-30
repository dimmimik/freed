from core.statistics import Statistics


class Expense:

    def __init__(self, amount, category):
        self.amount = amount
        self.category = category


def test_total():

    stats = Statistics()

    expenses = [
        Expense(20, "Food"),
        Expense(30, "Fuel")
    ]

    assert stats.total(expenses) == 50
