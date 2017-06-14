from confobo.persistence import schedule


class NoSuchDayError(Exception):
    pass


def get_schedule(date: str) -> str:
    """
    Return conference schedule for a given day

    :param date: date for which schedule has been requested

    :return: schedule for the date
    """
    if date not in schedule.get_conference_days():
        raise NoSuchDayError()
    return date
