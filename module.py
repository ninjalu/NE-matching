import pandas as pd
import numpy as np

STOP_WORDS = ['ltd', 'corp', 'plc', 'corporation', 'inc', 'co', 'group', 'company', 'companies', 'limited']

def standardise(df, col):
    """
    This function takes in dataframe and a column name, and perform the following:
    1. Remove '.'
    2. Lower case.
    3. Remove stop words

    and finally return standardised dataframe

    Args:
        df ([pd.DataFrame]): [description]
        col ([str]): [description]
    """
    df[f'{col}_sd'] = df[col].str.replace('.', '').str.lower()
    for word in STOP_WORDS:
        df[f'{col}_sd'] = df[f'{col}_sd'].str.replace(fr'\b{word}\b', '')
    return df

