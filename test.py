from datetime import timedelta, date


def daterange(start, end):
    return [start + timedelta(n) for n in range(int((end - start).days))]



print(daterange(date(2020, 10, 10), date(2020, 10, 1)))
