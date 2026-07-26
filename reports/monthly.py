class Monthly:

    def print(

        self,

        expenses

    ):

        print()

        print(

            "Monthly Records\n"

        )

        for item in expenses:

            print(

                item["month"],

                item["category"],

                item["amount"]

            )
