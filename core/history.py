class History:

    def sort_by_date(self, expenses):

        return sorted(
            expenses,
            key=lambda e: e.date
        )

    def latest(self, expenses, limit=10):

        return self.sort_by_date(expenses)[-limit:]
