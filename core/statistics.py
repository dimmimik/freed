from collections import defaultdict


class Statistics:

    def by_category(self, expenses):
        result = defaultdict(float)

        for expense in expenses:
            result[expense.category] += expense.amount

        return dict(result)

    def total(self, expenses):
        return sum(e.amount for e in expenses)

    def average(self, expenses):
        if not expenses:
            return 0

        return self.total(expenses) / len(expenses)
