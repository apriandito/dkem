# pip install pandasai

from pandasai import SmartDataframe
import pandas as pd

import os

os.environ['PANDASAI_API_KEY'] = '$2a$10$ldvJVbI0enZSEYYV2ySmGONS7NSv5UcLpqwXdNIdwDqGwDG.Dg75i'

df = pd.DataFrame({
    "country": [
        "United States",
        "United Kingdom",
        "France",
        "Germany",
        "Italy",
        "Spain",
        "Canada",
        "Australia",
        "Japan",
        "China",
    ],
    "gdp": [
        19294482071552,
        2891615567872,
        2411255037952,
        3435817336832,
        1745433788416,
        1181205135360,
        1607402389504,
        1490967855104,
        4380756541440,
        14631844184064,
    ],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12],
})

sdf = SmartDataframe(df)

print(sdf.chat("Return the average gdp"))

print(sdf.chat("What's the sum of the gdp of the 2 unhappiest countries?"))

print(sdf.chat("Plot a chart of the gdp by country sort from the highest"))