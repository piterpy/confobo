CONFERENCE_DAYS = ('2017-06-01', '2017-06-02')


class NoSuchDay(Exception):
    pass


def get_schedule(date: str) -> str:
    if date not in CONFERENCE_DAYS:
        raise NoSuchDay()
    return date
