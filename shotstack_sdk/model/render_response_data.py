"""
    Shotstack

    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON and a RESTful API.  You arrange and configure an edit and POST it to the API which will render your media and provide a file  location when complete.  For more details visit [shotstack.io](https://shotstack.io) or checkout our [getting started](https://shotstack.io/docs/guide/) documentation. There are two main API's, one for editing and generating assets (Edit API) and one for managing hosted assets (Serve API).  The Edit API base URL is: <b>https://api.shotstack.io/{version}</b>  The Serve API base URL is: <b>https://api.shotstack.io/serve/{version}</b>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from shotstack_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from shotstack_sdk.exceptions import ApiAttributeError


def lazy_import():
    from shotstack_sdk.model.edit import Edit
    globals()['Edit'] = Edit


class RenderResponseData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'QUEUED': "queued",
            'FETCHING': "fetching",
            'RENDERING': "rendering",
            'SAVING': "saving",
            'DONE': "done",
            'FAILED': "failed",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'data': (Edit,),  # noqa: E501
            'created': (str,),  # noqa: E501
            'updated': (str,),  # noqa: E501
            'plan': (str,),  # noqa: E501
            'error': (str,),  # noqa: E501
            'duration': (float,),  # noqa: E501
            'render_time': (float,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'poster': (str,),  # noqa: E501
            'thumbnail': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'status': 'status',  # noqa: E501
        'data': 'data',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'plan': 'plan',  # noqa: E501
        'error': 'error',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'render_time': 'renderTime',  # noqa: E501
        'url': 'url',  # noqa: E501
        'poster': 'poster',  # noqa: E501
        'thumbnail': 'thumbnail',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, owner, status, data, created, updated, *args, **kwargs):  # noqa: E501
        """RenderResponseData - a model defined in OpenAPI

        Args:
            id (str): The id of the render task in UUID format.
            owner (str): The owner id of the render task.
            status (str): The status of the render task. <ul>   <li>`queued` - render is queued waiting to be rendered</li>   <li>`fetching` - assets are being fetched</li>   <li>`rendering` - the asset is being rendered</li>   <li>`saving` - the final asset is being saved to storage</li>   <li>`done` - the asset is ready to be downloaded</li>   <li>`failed` - there was an error rendering the asset</li> </ul>
            data (Edit):
            created (str): The time the render task was initially queued.
            updated (str): The time the render status was last updated.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            plan (str): The customer subscription plan.. [optional]  # noqa: E501
            error (str): An error message, only displayed if an error occurred.. [optional]  # noqa: E501
            duration (float): The output video or audio length in seconds.. [optional]  # noqa: E501
            render_time (float): The time taken to render the asset in milliseconds.. [optional]  # noqa: E501
            url (str): The URL of the final asset. This will only be available if status is done. This is a temporary URL and will be deleted after 24 hours. By default all assets are copied to the Shotstack hosting and CDN destination.. [optional]  # noqa: E501
            poster (str): The URL of the poster image if requested. This will only be available if status is done.. [optional]  # noqa: E501
            thumbnail (str): The URL of the thumbnail image if requested. This will only be available if status is done.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.owner = owner
        self.status = status
        self.data = data
        self.created = created
        self.updated = updated
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, owner, status, data, created, updated, *args, **kwargs):  # noqa: E501
        """RenderResponseData - a model defined in OpenAPI

        Args:
            id (str): The id of the render task in UUID format.
            owner (str): The owner id of the render task.
            status (str): The status of the render task. <ul>   <li>`queued` - render is queued waiting to be rendered</li>   <li>`fetching` - assets are being fetched</li>   <li>`rendering` - the asset is being rendered</li>   <li>`saving` - the final asset is being saved to storage</li>   <li>`done` - the asset is ready to be downloaded</li>   <li>`failed` - there was an error rendering the asset</li> </ul>
            data (Edit):
            created (str): The time the render task was initially queued.
            updated (str): The time the render status was last updated.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            plan (str): The customer subscription plan.. [optional]  # noqa: E501
            error (str): An error message, only displayed if an error occurred.. [optional]  # noqa: E501
            duration (float): The output video or audio length in seconds.. [optional]  # noqa: E501
            render_time (float): The time taken to render the asset in milliseconds.. [optional]  # noqa: E501
            url (str): The URL of the final asset. This will only be available if status is done. This is a temporary URL and will be deleted after 24 hours. By default all assets are copied to the Shotstack hosting and CDN destination.. [optional]  # noqa: E501
            poster (str): The URL of the poster image if requested. This will only be available if status is done.. [optional]  # noqa: E501
            thumbnail (str): The URL of the thumbnail image if requested. This will only be available if status is done.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.owner = owner
        self.status = status
        self.data = data
        self.created = created
        self.updated = updated
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
