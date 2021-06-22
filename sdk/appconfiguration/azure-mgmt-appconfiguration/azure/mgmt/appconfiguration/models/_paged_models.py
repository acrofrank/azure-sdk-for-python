# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class ConfigurationStorePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ConfigurationStore <azure.mgmt.appconfiguration.models.ConfigurationStore>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ConfigurationStore]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConfigurationStorePaged, self).__init__(*args, **kwargs)
class ApiKeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApiKey <azure.mgmt.appconfiguration.models.ApiKey>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApiKey]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApiKeyPaged, self).__init__(*args, **kwargs)
class OperationDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`OperationDefinition <azure.mgmt.appconfiguration.models.OperationDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OperationDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationDefinitionPaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.appconfiguration.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.appconfiguration.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class KeyValuePaged(Paged):
    """
    A paging container for iterating over a list of :class:`KeyValue <azure.mgmt.appconfiguration.models.KeyValue>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[KeyValue]'}
    }

    def __init__(self, *args, **kwargs):

        super(KeyValuePaged, self).__init__(*args, **kwargs)
