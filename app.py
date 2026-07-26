from config import *

from core.tracker import Tracker
from core.calculator import Calculator
from core.filters import Filters
from core.exporter import Exporter

from reports.summary import Summary
from reports.monthly import Monthly

expenses=Tracker().load()

expenses=[

    e

    for e in expenses

    if __import__("utils.validator").validator.Validator().valid(e)

]

calculator=Calculator()

totals=calculator.by_category(

    expenses

)

overall=calculator.total(

    expenses

)

report=Summary().build(

    totals,

    overall,

    CURRENCY

)

print(report)

Monthly().print(

    Filters().month(

        expenses,

        "July"

    )

)

Exporter().save(

    report,

    REPORT_FILE

)
