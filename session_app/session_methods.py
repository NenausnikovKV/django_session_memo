import copy
from collections import namedtuple

from django.http import QueryDict


class SessionManager:
    """
        Session dictionary manager.
        It contains methods for user defined session items.
    """

    #  session variable keys
    Item = namedtuple('Item', ['name', 'value'])
    VISIT_COUNT = Item(name="visit_count", value=0)
    ITEMS = {VISIT_COUNT.name: VISIT_COUNT.value}

    def __init__(self, session: QueryDict):
        assert session
        self.session = copy.deepcopy(session)
        for session_item in self.ITEMS:
            self.session[session_item.name] = session_item.value

    def increase_request_session_count_by_one(self):
        visit_count = self.request_session_count
        new_visit_count = visit_count + 1
        self.request_session_count = new_visit_count

    @property
    def request_session_count(self):
        visit_count = self.session[self.VISIT_COUNT.name]
        return visit_count

    @request_session_count.setter
    def request_session_count(self, value):
        self.session[self.VISIT_COUNT.name] = value


VISIT_COUNT = "visit_count"


def get_request_session_count(session):
    visit_count = session.get(VISIT_COUNT, 0)
    return visit_count


def get_request_sessiosn_count(request):
    visit_count = request.session.get("visit_count", 0)
    return visit_count


def create_new_session_count(session, value):
    assert session
    assert session.get(VISIT_COUNT, None) is not None
    new_session = copy.deepcopy(session)
    new_session[VISIT_COUNT] = value
    return new_session
