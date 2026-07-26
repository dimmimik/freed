class Exporter:

    def save(

        self,

        text,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf8"

        ) as file:

            file.write(text)
