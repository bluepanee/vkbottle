# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class LeadsCheckUser(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        lead_id: int,
        test_result: int,
        test_mode: bool,
        auto_start: bool,
        age: int,
        country: str,
    ) -> responses.leads.CheckUser:
        """ leads.checkUser
        From Vk Docs: Checks if the user can start the lead.
        Access from user token(s)
        :param lead_id: Lead ID.
        :param test_result: Value to be return in 'result' field when test mode is used.
        :param test_mode: 
        :param auto_start: 
        :param age: User age.
        :param country: User country code.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.checkUser", params, response_model=responses.leads.CheckUser
        )


class LeadsComplete(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self, vk_sid: str, secret: str, comment: str
    ) -> responses.leads.Complete:
        """ leads.complete
        From Vk Docs: Completes the lead started by user.
        Access from user, service token(s)
        :param vk_sid: Session obtained as GET parameter when session started.
        :param secret: Secret key from the lead testing interface.
        :param comment: Comment text.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.complete", params, response_model=responses.leads.Complete
        )


class LeadsGetStats(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, lead_id: int, secret: str, date_start: str, date_end: str
    ) -> responses.leads.GetStats:
        """ leads.getStats
        From Vk Docs: Returns lead stats data.
        Access from user token(s)
        :param lead_id: Lead ID.
        :param secret: Secret key obtained from the lead testing interface.
        :param date_start: Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.getStats", params, response_model=responses.leads.GetStats
        )


class LeadsGetUsers(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        offer_id: int,
        secret: str,
        offset: int,
        count: int,
        status: int,
        reverse: bool,
    ) -> responses.leads.GetUsers:
        """ leads.getUsers
        From Vk Docs: Returns a list of last user actions for the offer.
        Access from user, service token(s)
        :param offer_id: Offer ID.
        :param secret: Secret key obtained in the lead testing interface.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param status: Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.getUsers", params, response_model=responses.leads.GetUsers
        )


class LeadsMetricHit(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, data: str) -> responses.leads.MetricHit:
        """ leads.metricHit
        From Vk Docs: Counts the metric event.
        Access from user token(s)
        :param data: Metric data obtained in the lead interface.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.metricHit", params, response_model=responses.leads.MetricHit
        )


class LeadsStart(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        lead_id: int,
        secret: str,
        uid: int,
        aid: int,
        test_mode: bool,
        force: bool,
    ) -> responses.leads.Start:
        """ leads.start
        From Vk Docs: Creates new session for the user passing the offer.
        Access from user, service token(s)
        :param lead_id: Lead ID.
        :param secret: Secret key from the lead testing interface.
        :param uid: 
        :param aid: 
        :param test_mode: 
        :param force: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "leads.start", params, response_model=responses.leads.Start
        )


class Leads:
    def __init__(self, request):
        self.check_user = LeadsCheckUser(request)
        self.complete = LeadsComplete(request)
        self.get_stats = LeadsGetStats(request)
        self.get_users = LeadsGetUsers(request)
        self.metric_hit = LeadsMetricHit(request)
        self.start = LeadsStart(request)