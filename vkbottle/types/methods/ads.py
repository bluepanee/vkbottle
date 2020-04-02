# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class AdsAddOfficeUsers(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.addOfficeUsers
        From Vk Docs: Adds managers and/or supervisors to advertising account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.addOfficeUsers", params)


class AdsCheckLink(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, account_id: int, link_type: str, link_url: str, campaign_id: int
    ):
        """ ads.checkLink
        From Vk Docs: Allows to check the ad link.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.checkLink", params)


class AdsCreateAds(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.createAds
        From Vk Docs: Creates ads.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.createAds", params)


class AdsCreateCampaigns(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.createCampaigns
        From Vk Docs: Creates advertising campaigns.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.createCampaigns", params)


class AdsCreateClients(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.createClients
        From Vk Docs: Creates clients of an advertising agency.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.createClients", params)


class AdsCreateTargetGroup(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        client_id: int,
        name: str,
        lifetime: int,
        target_pixel_id: int,
        target_pixel_rules: str,
    ):
        """ ads.createTargetGroup
        From Vk Docs: Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.).
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param name: Name of the target group — a string up to 64 characters long.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param target_pixel_id: 
        :param target_pixel_rules: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.createTargetGroup", params)


class AdsDeleteAds(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ids: str):
        """ ads.deleteAds
        From Vk Docs: Archives ads.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.deleteAds", params)


class AdsDeleteCampaigns(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ids: str):
        """ ads.deleteCampaigns
        From Vk Docs: Archives advertising campaigns.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.deleteCampaigns", params)


class AdsDeleteClients(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ids: str):
        """ ads.deleteClients
        From Vk Docs: Archives clients of an advertising agency.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.deleteClients", params)


class AdsDeleteTargetGroup(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, client_id: int, target_group_id: int):
        """ ads.deleteTargetGroup
        From Vk Docs: Deletes a retarget group.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Group ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.deleteTargetGroup", params)


class AdsGetAccounts(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,):
        """ ads.getAccounts
        From Vk Docs: Returns a list of advertising accounts.
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getAccounts", params)


class AdsGetAds(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        ad_ids: str,
        campaign_ids: str,
        client_id: int,
        include_deleted: bool,
        limit: int,
        offset: int,
    ):
        """ ads.getAds
        From Vk Docs: Returns number of ads.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getAds", params)


class AdsGetAdsLayout(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        ad_ids: str,
        campaign_ids: str,
        client_id: int,
        include_deleted: bool,
        limit: int,
        offset: int,
    ):
        """ ads.getAdsLayout
        From Vk Docs: Returns descriptions of ad layouts.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getAdsLayout", params)


class AdsGetAdsTargeting(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        ad_ids: str,
        campaign_ids: str,
        client_id: int,
        include_deleted: bool,
        limit: int,
        offset: int,
    ):
        """ ads.getAdsTargeting
        From Vk Docs: Returns ad targeting parameters.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getAdsTargeting", params)


class AdsGetBudget(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int):
        """ ads.getBudget
        From Vk Docs: Returns current budget of the advertising account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getBudget", params)


class AdsGetCampaigns(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, account_id: int, client_id: int, include_deleted: bool, campaign_ids: str
    ):
        """ ads.getCampaigns
        From Vk Docs: Returns a list of campaigns in an advertising account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getCampaigns", params)


class AdsGetCategories(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, lang: str):
        """ ads.getCategories
        From Vk Docs: Returns a list of possible ad categories.
        Access from user token(s)
        :param lang: Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getCategories", params)


class AdsGetClients(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int):
        """ ads.getClients
        From Vk Docs: Returns a list of advertising agency's clients.
        Access from user token(s)
        :param account_id: Advertising account ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getClients", params)


class AdsGetDemographics(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
    ):
        """ ads.getDemographics
        From Vk Docs: Returns demographics for ads or campaigns.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getDemographics", params)


class AdsGetFloodStats(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int):
        """ ads.getFloodStats
        From Vk Docs: Returns information about current state of a counter — number of remaining runs of methods and time to the next counter nulling in seconds.
        Access from user token(s)
        :param account_id: Advertising account ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getFloodStats", params)


class AdsGetOfficeUsers(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int):
        """ ads.getOfficeUsers
        From Vk Docs: Returns a list of managers and supervisors of advertising account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getOfficeUsers", params)


class AdsGetPostsReach(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ids_type: str, ids: str):
        """ ads.getPostsReach
        From Vk Docs: Returns detailed statistics of promoted posts reach from campaigns and ads.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getPostsReach", params)


class AdsGetRejectionReason(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ad_id: int):
        """ ads.getRejectionReason
        From Vk Docs: Returns a reason of ad rejection for pre-moderation.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getRejectionReason", params)


class AdsGetStatistics(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
    ):
        """ ads.getStatistics
        From Vk Docs: Returns statistics of performance indicators for ads, campaigns, clients or the whole account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns,, *client — clients,, *office — account.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getStatistics", params)


class AdsGetSuggestions(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, section: str, ids: str, q: str, country: int, cities: str, lang: str
    ):
        """ ads.getSuggestions
        From Vk Docs: Returns a set of auto-suggestions for various targeting parameters.
        Access from user token(s)
        :param section: Section, suggestions are retrieved in. Available values: *countries — request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions — requested list of regions. 'country' parameter is required. *cities — requested list of cities. 'country' parameter is required. *districts — requested list of districts. 'cities' parameter is required. *stations — requested list of subway stations. 'cities' parameter is required. *streets — requested list of streets. 'cities' parameter is required. *schools — requested list of educational organizations. 'cities' parameter is required. *interests — requested list of interests. *positions — requested list of positions (professions). *group_types — requested list of group types. *religions — requested list of religious commitments. *browsers — requested list of browsers and mobile devices.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: ID of the country objects are searched in.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param lang: Language of the returned string values. Supported languages: *ru — Russian,, *ua — Ukrainian,, *en — English.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getSuggestions", params)


class AdsGetTargetGroups(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, client_id: int, extended: bool):
        """ ads.getTargetGroups
        From Vk Docs: Returns a list of target groups.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' — to return pixel code.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getTargetGroups", params)


class AdsGetTargetingStats(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        client_id: int,
        criteria: str,
        ad_id: int,
        ad_format: int,
        ad_platform: str,
        ad_platform_no_wall: str,
        ad_platform_no_ad_network: str,
        link_url: str,
        link_domain: str,
    ):
        """ ads.getTargetingStats
        From Vk Docs: Returns the size of targeting audience, and also recommended values for CPC and CPM.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_format: Ad format. Possible values: *'1' — image and text,, *'2' — big image,, *'3' — exclusive format,, *'4' — community, square image,, *'7' — special app format,, *'8' — special community format,, *'9' — post in community,, *'10' — app board.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' — VK and partner sites,, *'1' — VK only. (for 'ad_format' = '9'), *'all' — all platforms,, *'desktop' — desktop version,, *'mobile' — mobile version and apps.
        :param ad_platform_no_wall: 
        :param ad_platform_no_ad_network: 
        :param link_url: URL for the advertised object.
        :param link_domain: Domain of the advertised object.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getTargetingStats", params)


class AdsGetUploadURL(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, ad_format: int, icon: int):
        """ ads.getUploadURL
        From Vk Docs: Returns URL to upload an ad photo to.
        Access from user token(s)
        :param ad_format: Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
        :param icon: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getUploadURL", params)


class AdsGetVideoUploadURL(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,):
        """ ads.getVideoUploadURL
        From Vk Docs: Returns URL to upload an ad video to.
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.getVideoUploadURL", params)


class AdsImportTargetContacts(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, account_id: int, client_id: int, target_group_id: int, contacts: str
    ):
        """ ads.importTargetContacts
        From Vk Docs: Imports a list of advertiser's contacts to count VK registered users against the target group.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Target group ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.importTargetContacts", params)


class AdsRemoveOfficeUsers(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, ids: str):
        """ ads.removeOfficeUsers
        From Vk Docs: Removes managers and/or supervisors from advertising account.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.removeOfficeUsers", params)


class AdsUpdateAds(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.updateAds
        From Vk Docs: Edits ads.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.updateAds", params)


class AdsUpdateCampaigns(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.updateCampaigns
        From Vk Docs: Edits advertising campaigns.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.updateCampaigns", params)


class AdsUpdateClients(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, account_id: int, data: str):
        """ ads.updateClients
        From Vk Docs: Edits clients of an advertising agency.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.updateClients", params)


class AdsUpdateTargetGroup(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        account_id: int,
        client_id: int,
        target_group_id: int,
        name: str,
        domain: str,
        lifetime: int,
        target_pixel_id: int,
        target_pixel_rules: str,
    ):
        """ ads.updateTargetGroup
        From Vk Docs: Edits a retarget group.
        Access from user token(s)
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Group ID.
        :param name: New name of the target group — a string up to 64 characters long.
        :param domain: Domain of the site where user accounting code will be placed.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' – automatic exclusion is off.
        :param target_pixel_id: 
        :param target_pixel_rules: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("ads.updateTargetGroup", params)


class Ads:
    def __init__(self, request):
        self.add_office_users = AdsAddOfficeUsers(request)
        self.check_link = AdsCheckLink(request)
        self.create_ads = AdsCreateAds(request)
        self.create_campaigns = AdsCreateCampaigns(request)
        self.create_clients = AdsCreateClients(request)
        self.create_target_group = AdsCreateTargetGroup(request)
        self.delete_ads = AdsDeleteAds(request)
        self.delete_campaigns = AdsDeleteCampaigns(request)
        self.delete_clients = AdsDeleteClients(request)
        self.delete_target_group = AdsDeleteTargetGroup(request)
        self.get_accounts = AdsGetAccounts(request)
        self.get_ads = AdsGetAds(request)
        self.get_ads_layout = AdsGetAdsLayout(request)
        self.get_ads_targeting = AdsGetAdsTargeting(request)
        self.get_budget = AdsGetBudget(request)
        self.get_campaigns = AdsGetCampaigns(request)
        self.get_categories = AdsGetCategories(request)
        self.get_clients = AdsGetClients(request)
        self.get_demographics = AdsGetDemographics(request)
        self.get_flood_stats = AdsGetFloodStats(request)
        self.get_office_users = AdsGetOfficeUsers(request)
        self.get_posts_reach = AdsGetPostsReach(request)
        self.get_rejection_reason = AdsGetRejectionReason(request)
        self.get_statistics = AdsGetStatistics(request)
        self.get_suggestions = AdsGetSuggestions(request)
        self.get_target_groups = AdsGetTargetGroups(request)
        self.get_targeting_stats = AdsGetTargetingStats(request)
        self.get_upload_u_r_l = AdsGetUploadURL(request)
        self.get_video_upload_u_r_l = AdsGetVideoUploadURL(request)
        self.import_target_contacts = AdsImportTargetContacts(request)
        self.remove_office_users = AdsRemoveOfficeUsers(request)
        self.update_ads = AdsUpdateAds(request)
        self.update_campaigns = AdsUpdateCampaigns(request)
        self.update_clients = AdsUpdateClients(request)
        self.update_target_group = AdsUpdateTargetGroup(request)