class Calculator:

    def total(

        self,

        expenses

    ):

        return sum(

            item["amount"]

            for item in expenses

        )

    def by_category(

        self,

        expenses

    ):

        result={}

        for item in expenses:

            result.setdefault(

                item["category"],

                0

            )

            result[

                item["category"]

            ]+=item["amount"]

        return result
