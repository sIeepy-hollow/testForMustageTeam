from pandas import DataFrame


def save_data_to_xlsx(df: DataFrame):
    df.to_excel("exchange_rates.xlsx", index=False, engine='openpyxl')
