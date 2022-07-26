import pandas as pd


def add_two_numbers(a: int, b: int) -> int:
    return a + b


################################# ciencia de datos
### 111111 222222 3333 444444 555555


class Cleaning(object):
    def __init__(self, df: pd.DataFrame, variable: str):
        self.data = df
        self.id = variable

    def remmove_invalid_id(self) -> pd.DataFrame:
        df_cleaning = self.data.drop_duplicates().copy()
        id_remover = [int(str(x) * y) for x in range(10) for y in range(4, 9)]
        df_final = df_cleaning[~df_cleaning[self.id].isin(id_remover)]
        return df_final


clean = Cleaning(
    df=pd.DataFrame({"identificacion": [1, 2, 3, 4, 5555555, 66666]}),
    variable="identificacion",
)
clean.remmove_invalid_id()
