class Summary:

    def build(

        self,

        totals,

        overall,

        currency

    ):

        lines=[]

        lines.append(

            "Expense Summary\n"

        )

        for category,value in totals.items():

            lines.append(

                f"{category:<18}{currency}{value:.2f}"

            )

        lines.append("")

        lines.append(

            f"Total: {currency}{overall:.2f}"

        )

        return "\n".join(lines)
