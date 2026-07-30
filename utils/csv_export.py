import csv


class CsvExport:

    def export(self, expenses, filename):

        with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Category",
                "Amount",
                "Description"
            ])

            for expense in expenses:

                writer.writerow([
                    expense.date,
                    expense.category,
                    expense.amount,
                    expense.description
                ])
