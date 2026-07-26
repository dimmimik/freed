class Filters:

    def month(

        self,

        expenses,

        name

    ):

        return [

            item

            for item in expenses

            if item["month"]==name

        ]
