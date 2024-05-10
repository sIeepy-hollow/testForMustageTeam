from datetime import date, datetime, timedelta

import pandas as pd

from models import session, ExchangeRate


def read_data_from_db():
    today = date.today()

    result = session.query(ExchangeRate).filter(
        ExchangeRate.datetime >= datetime(today.year, today.month, today.day),
        ExchangeRate.datetime < datetime(today.year, today.month, today.day) + timedelta(days=1)
    ).all()

    data = [{
        "id": record.id,
        "datetime": record.datetime.strftime("%d.%m.%Y %H:%M:%S"),
        "exchange_rate": record.exchange_rate
    } for record in result]

    df = pd.DataFrame(data)
    return df


def get_rate(datetime_value: datetime) -> ExchangeRate | None:
    return session.query(ExchangeRate).filter(ExchangeRate.datetime == datetime_value).first()
