# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    scope: str,
    *,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    filter: Optional[str] = None,
    apply: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{scope}/providers/Microsoft.Consumption/charges')
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if start_date is not None:
        query_parameters['startDate'] = _SERIALIZER.query("start_date", start_date, 'str')
    if end_date is not None:
        query_parameters['endDate'] = _SERIALIZER.query("end_date", end_date, 'str')
    if filter is not None:
        query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')
    if apply is not None:
        query_parameters['$apply'] = _SERIALIZER.query("apply", apply, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class ChargesOperations(object):
    """ChargesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.consumption.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        scope: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        filter: Optional[str] = None,
        apply: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ChargesListResult":
        """Lists the charges based for the defined scope.

        :param scope: The scope associated with charges operations. This includes
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope. For department and enrollment accounts, you can also add billing
         period to the scope using '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'.
         For e.g. to specify billing period at department scope use
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'.
         Also, Modern Commerce Account scopes are
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for billingAccount scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param start_date: Start date.
        :type start_date: str
        :param end_date: End date.
        :type end_date: str
        :param filter: May be used to filter charges by properties/usageEnd (Utc time),
         properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'.
         It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where
         key and value is separated by a colon (:).
        :type filter: str
        :param apply: May be used to group charges for billingAccount scope by
         properties/billingProfileId, properties/invoiceSectionId, properties/customerId (specific for
         Partner Led), or for billingProfile scope by properties/invoiceSectionId.
        :type apply: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ChargesListResult, or the result of cls(response)
        :rtype: ~azure.mgmt.consumption.models.ChargesListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ChargesListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            scope=scope,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            apply=apply,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ChargesListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/{scope}/providers/Microsoft.Consumption/charges'}  # type: ignore

