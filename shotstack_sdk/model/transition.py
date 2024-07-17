"""
    Shotstack

    Official Python SDK for the Shotstack Cloud Video Editing API

    The version of the OpenAPI document: v1
    Contact: pypi@shotstack.io
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



class Transition(ModelNormal):
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
        ('_in',): {
            'FADE': "fade",
            'FADESLOW': "fadeSlow",
            'FADEFAST': "fadeFast",
            'REVEAL': "reveal",
            'REVEALSLOW': "revealSlow",
            'REVEALFAST': "revealFast",
            'WIPELEFT': "wipeLeft",
            'WIPELEFTSLOW': "wipeLeftSlow",
            'WIPELEFTFAST': "wipeLeftFast",
            'WIPERIGHT': "wipeRight",
            'WIPERIGHTSLOW': "wipeRightSlow",
            'WIPERIGHTFAST': "wipeRightFast",
            'SLIDELEFT': "slideLeft",
            'SLIDELEFTSLOW': "slideLeftSlow",
            'SLIDELEFTFAST': "slideLeftFast",
            'SLIDERIGHT': "slideRight",
            'SLIDERIGHTSLOW': "slideRightSlow",
            'SLIDERIGHTFAST': "slideRightFast",
            'SLIDEUP': "slideUp",
            'SLIDEUPSLOW': "slideUpSlow",
            'SLIDEUPFAST': "slideUpFast",
            'SLIDEDOWN': "slideDown",
            'SLIDEDOWNSLOW': "slideDownSlow",
            'SLIDEDOWNFAST': "slideDownFast",
            'CAROUSELLEFT': "carouselLeft",
            'CAROUSELLEFTSLOW': "carouselLeftSlow",
            'CAROUSELLEFTFAST': "carouselLeftFast",
            'CAROUSELRIGHT': "carouselRight",
            'CAROUSELRIGHTSLOW': "carouselRightSlow",
            'CAROUSELRIGHTFAST': "carouselRightFast",
            'CAROUSELUP': "carouselUp",
            'CAROUSELUPSLOW': "carouselUpSlow",
            'CAROUSELUPFAST': "carouselUpFast",
            'CAROUSELDOWN': "carouselDown",
            'CAROUSELDOWNSLOW': "carouselDownSlow",
            'CAROUSELDOWNFAST': "carouselDownFast",
            'SHUFFLETOPRIGHT': "shuffleTopRight",
            'SHUFFLETOPRIGHTSLOW': "shuffleTopRightSlow",
            'SHUFFLETOPRIGHTFAST': "shuffleTopRightFast",
            'SHUFFLERIGHTTOP': "shuffleRightTop",
            'SHUFFLERIGHTTOPSLOW': "shuffleRightTopSlow",
            'SHUFFLERIGHTTOPFAST': "shuffleRightTopFast",
            'SHUFFLERIGHTBOTTOM': "shuffleRightBottom",
            'SHUFFLERIGHTBOTTOMSLOW': "shuffleRightBottomSlow",
            'SHUFFLERIGHTBOTTOMFAST': "shuffleRightBottomFast",
            'SHUFFLEBOTTOMRIGHT': "shuffleBottomRight",
            'SHUFFLEBOTTOMRIGHTSLOW': "shuffleBottomRightSlow",
            'SHUFFLEBOTTOMRIGHTFAST': "shuffleBottomRightFast",
            'SHUFFLEBOTTOMLEFT': "shuffleBottomLeft",
            'SHUFFLEBOTTOMLEFTSLOW': "shuffleBottomLeftSlow",
            'SHUFFLEBOTTOMLEFTFAST': "shuffleBottomLeftFast",
            'SHUFFLELEFTBOTTOM': "shuffleLeftBottom",
            'SHUFFLELEFTBOTTOMSLOW': "shuffleLeftBottomSlow",
            'SHUFFLELEFTBOTTOMFAST': "shuffleLeftBottomFast",
            'SHUFFLELEFTTOP': "shuffleLeftTop",
            'SHUFFLELEFTTOPSLOW': "shuffleLeftTopSlow",
            'SHUFFLELEFTTOPFAST': "shuffleLeftTopFast",
            'SHUFFLETOPLEFT': "shuffleTopLeft",
            'SHUFFLETOPLEFTSLOW': "shuffleTopLeftSlow",
            'SHUFFLETOPLEFTFAST': "shuffleTopLeftFast",
            'ZOOM': "zoom",
        },
        ('out',): {
            'FADE': "fade",
            'FADESLOW': "fadeSlow",
            'FADEFAST': "fadeFast",
            'REVEAL': "reveal",
            'REVEALSLOW': "revealSlow",
            'REVEALFAST': "revealFast",
            'WIPELEFT': "wipeLeft",
            'WIPELEFTSLOW': "wipeLeftSlow",
            'WIPELEFTFAST': "wipeLeftFast",
            'WIPERIGHT': "wipeRight",
            'WIPERIGHTSLOW': "wipeRightSlow",
            'WIPERIGHTFAST': "wipeRightFast",
            'SLIDELEFT': "slideLeft",
            'SLIDELEFTSLOW': "slideLeftSlow",
            'SLIDELEFTFAST': "slideLeftFast",
            'SLIDERIGHT': "slideRight",
            'SLIDERIGHTSLOW': "slideRightSlow",
            'SLIDERIGHTFAST': "slideRightFast",
            'SLIDEUP': "slideUp",
            'SLIDEUPSLOW': "slideUpSlow",
            'SLIDEUPFAST': "slideUpFast",
            'SLIDEDOWN': "slideDown",
            'SLIDEDOWNSLOW': "slideDownSlow",
            'SLIDEDOWNFAST': "slideDownFast",
            'CAROUSELLEFT': "carouselLeft",
            'CAROUSELLEFTSLOW': "carouselLeftSlow",
            'CAROUSELLEFTFAST': "carouselLeftFast",
            'CAROUSELRIGHT': "carouselRight",
            'CAROUSELRIGHTSLOW': "carouselRightSlow",
            'CAROUSELRIGHTFAST': "carouselRightFast",
            'CAROUSELUP': "carouselUp",
            'CAROUSELUPSLOW': "carouselUpSlow",
            'CAROUSELUPFAST': "carouselUpFast",
            'CAROUSELDOWN': "carouselDown",
            'CAROUSELDOWNSLOW': "carouselDownSlow",
            'CAROUSELDOWNFAST': "carouselDownFast",
            'SHUFFLETOPRIGHT': "shuffleTopRight",
            'SHUFFLETOPRIGHTSLOW': "shuffleTopRightSlow",
            'SHUFFLETOPRIGHTFAST': "shuffleTopRightFast",
            'SHUFFLERIGHTTOP': "shuffleRightTop",
            'SHUFFLERIGHTTOPSLOW': "shuffleRightTopSlow",
            'SHUFFLERIGHTTOPFAST': "shuffleRightTopFast",
            'SHUFFLERIGHTBOTTOM': "shuffleRightBottom",
            'SHUFFLERIGHTBOTTOMSLOW': "shuffleRightBottomSlow",
            'SHUFFLERIGHTBOTTOMFAST': "shuffleRightBottomFast",
            'SHUFFLEBOTTOMRIGHT': "shuffleBottomRight",
            'SHUFFLEBOTTOMRIGHTSLOW': "shuffleBottomRightSlow",
            'SHUFFLEBOTTOMRIGHTFAST': "shuffleBottomRightFast",
            'SHUFFLEBOTTOMLEFT': "shuffleBottomLeft",
            'SHUFFLEBOTTOMLEFTSLOW': "shuffleBottomLeftSlow",
            'SHUFFLEBOTTOMLEFTFAST': "shuffleBottomLeftFast",
            'SHUFFLELEFTBOTTOM': "shuffleLeftBottom",
            'SHUFFLELEFTBOTTOMSLOW': "shuffleLeftBottomSlow",
            'SHUFFLELEFTBOTTOMFAST': "shuffleLeftBottomFast",
            'SHUFFLELEFTTOP': "shuffleLeftTop",
            'SHUFFLELEFTTOPSLOW': "shuffleLeftTopSlow",
            'SHUFFLELEFTTOPFAST': "shuffleLeftTopFast",
            'SHUFFLETOPLEFT': "shuffleTopLeft",
            'SHUFFLETOPLEFTSLOW': "shuffleTopLeftSlow",
            'SHUFFLETOPLEFTFAST': "shuffleTopLeftFast",
            'ZOOM': "zoom",
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
        return {
            '_in': (str,),  # noqa: E501
            'out': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        '_in': 'in',  # noqa: E501
        'out': 'out',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transition - a model defined in OpenAPI

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
            _in (str): The transition in. Available transitions are:   <ul>     <li>`fade` - fade in</li>     <li>`reveal` - reveal from left to right</li>     <li>`wipeLeft` - fade across screen to the left</li>     <li>`wipeRight` - fade across screen to the right</li>     <li>`slideLeft` - move slightly left and fade in</li>     <li>`slideRight` - move slightly right and fade in</li>     <li>`slideUp` - move slightly up and fade in</li>     <li>`slideDown` - move slightly down and fade in</li>     <li>`carouselLeft` - slide in from right to left</li>     <li>`carouselRight` - slide in from left to right</li>     <li>`carouselUp` - slide in from bottom to top</li>     <li>`carouselDown` - slide in from top to bottom</li>     <li>`shuffleTopRight` - rotate in from top right</li>     <li>`shuffleRightTop` - rotate in from right top</li>     <li>`shuffleRightBottom` - rotate in from right bottom</li>     <li>`shuffleBottomRight` - rotate in from bottom right</li>     <li>`shuffleBottomLeft` - rotate in from bottom left</li>     <li>`shuffleLeftBottom` - rotate in from left bottom</li>     <li>`shuffleLeftTop` - rotate in from left top</li>     <li>`shuffleTopLeft` - rotate in from top left</li>     <li>`zoom` - fast zoom in</li>   </ul> The transition speed can also be controlled by appending `Fast` or `Slow` to the transition, e.g. `fadeFast` or `CarouselLeftSlow`.. [optional]  # noqa: E501
            out (str): The transition out. Available transitions are:   <ul>     <li>`fade` - fade out</li>     <li>`reveal` - reveal from right to left</li>     <li>`wipeLeft` - fade across screen to the left</li>     <li>`wipeRight` - fade across screen to the right</li>     <li>`slideLeft` - move slightly left and fade out</li>     <li>`slideRight` - move slightly right and fade out</li>     <li>`slideUp` - move slightly up and fade out</li>     <li>`slideDown` - move slightly down and fade out</li>     <li>`carouselLeft` - slide out from right to left</li>     <li>`carouselRight` - slide out from left to right</li>     <li>`carouselUp` - slide out from bottom to top</li>     <li>`carouselDown` - slide out from top  to bottom</li>     <li>`shuffleTopRight` - rotate out from top right</li>     <li>`shuffleRightTop` - rotate out from right top</li>     <li>`shuffleRightBottom` - rotate out from right bottom</li>     <li>`shuffleBottomRight` - rotate out from bottom right</li>     <li>`shuffleBottomLeft` - rotate out from bottom left</li>     <li>`shuffleLeftBottom` - rotate out from left bottom</li>     <li>`shuffleLeftTop` - rotate out from left top</li>     <li>`shuffleTopLeft` - rotate out from top left</li>     <li>`zoom` - fast zoom out</li>   </ul> The transition speed can also be controlled by appending `Fast` or `Slow` to the transition, e.g. `fadeFast` or `CarouselLeftSlow`.. [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Transition - a model defined in OpenAPI

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
            _in (str): The transition in. Available transitions are:   <ul>     <li>`fade` - fade in</li>     <li>`reveal` - reveal from left to right</li>     <li>`wipeLeft` - fade across screen to the left</li>     <li>`wipeRight` - fade across screen to the right</li>     <li>`slideLeft` - move slightly left and fade in</li>     <li>`slideRight` - move slightly right and fade in</li>     <li>`slideUp` - move slightly up and fade in</li>     <li>`slideDown` - move slightly down and fade in</li>     <li>`carouselLeft` - slide in from right to left</li>     <li>`carouselRight` - slide in from left to right</li>     <li>`carouselUp` - slide in from bottom to top</li>     <li>`carouselDown` - slide in from top to bottom</li>     <li>`shuffleTopRight` - rotate in from top right</li>     <li>`shuffleRightTop` - rotate in from right top</li>     <li>`shuffleRightBottom` - rotate in from right bottom</li>     <li>`shuffleBottomRight` - rotate in from bottom right</li>     <li>`shuffleBottomLeft` - rotate in from bottom left</li>     <li>`shuffleLeftBottom` - rotate in from left bottom</li>     <li>`shuffleLeftTop` - rotate in from left top</li>     <li>`shuffleTopLeft` - rotate in from top left</li>     <li>`zoom` - fast zoom in</li>   </ul> The transition speed can also be controlled by appending `Fast` or `Slow` to the transition, e.g. `fadeFast` or `CarouselLeftSlow`.. [optional]  # noqa: E501
            out (str): The transition out. Available transitions are:   <ul>     <li>`fade` - fade out</li>     <li>`reveal` - reveal from right to left</li>     <li>`wipeLeft` - fade across screen to the left</li>     <li>`wipeRight` - fade across screen to the right</li>     <li>`slideLeft` - move slightly left and fade out</li>     <li>`slideRight` - move slightly right and fade out</li>     <li>`slideUp` - move slightly up and fade out</li>     <li>`slideDown` - move slightly down and fade out</li>     <li>`carouselLeft` - slide out from right to left</li>     <li>`carouselRight` - slide out from left to right</li>     <li>`carouselUp` - slide out from bottom to top</li>     <li>`carouselDown` - slide out from top  to bottom</li>     <li>`shuffleTopRight` - rotate out from top right</li>     <li>`shuffleRightTop` - rotate out from right top</li>     <li>`shuffleRightBottom` - rotate out from right bottom</li>     <li>`shuffleBottomRight` - rotate out from bottom right</li>     <li>`shuffleBottomLeft` - rotate out from bottom left</li>     <li>`shuffleLeftBottom` - rotate out from left bottom</li>     <li>`shuffleLeftTop` - rotate out from left top</li>     <li>`shuffleTopLeft` - rotate out from top left</li>     <li>`zoom` - fast zoom out</li>   </ul> The transition speed can also be controlled by appending `Fast` or `Slow` to the transition, e.g. `fadeFast` or `CarouselLeftSlow`.. [optional]  # noqa: E501
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
