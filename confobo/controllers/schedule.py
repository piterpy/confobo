from confobo.persistence import schedule


class NoSuchDayError(Exception):
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return '`{}` is not one of the conference days.'.format(self.date)


def get_schedule(date: str) -> str:
    """
    Return conference schedule for a given day

    :param date: date for which schedule has been requested

    :return: schedule for the date
    """
    if date not in schedule.get_conference_days():
        raise NoSuchDayError(date)
    return 'Schedule for {}'.format(date)
