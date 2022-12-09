"""
    Shotstack

    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON and a RESTful API.  You arrange and configure an edit and POST it to the API which will render your media and provide a file  location when complete.  For more details visit [shotstack.io](https://shotstack.io) or checkout our [getting started](https://shotstack.io/docs/guide/) documentation.  There are two main API's, one for editing and generating assets (Edit API) and one for managing hosted assets (Serve API).  The Edit API base URL is: <b>https://api.shotstack.io/{version}</b>  The Serve API base URL is: <b>https://api.shotstack.io/serve/{version}</b>   # noqa: E501

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
    from shotstack_sdk.model.asset import Asset
    from shotstack_sdk.model.offset import Offset
    from shotstack_sdk.model.transformation import Transformation
    from shotstack_sdk.model.transition import Transition
    globals()['Asset'] = Asset
    globals()['Offset'] = Offset
    globals()['Transformation'] = Transformation
    globals()['Transition'] = Transition


class Clip(ModelNormal):
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
        ('fit',): {
            'COVER': "cover",
            'CONTAIN': "contain",
            'CROP': "crop",
            'NONE': "none",
        },
        ('position',): {
            'TOP': "top",
            'TOPRIGHT': "topRight",
            'RIGHT': "right",
            'BOTTOMRIGHT': "bottomRight",
            'BOTTOM': "bottom",
            'BOTTOMLEFT': "bottomLeft",
            'LEFT': "left",
            'TOPLEFT': "topLeft",
            'CENTER': "center",
        },
        ('effect',): {
            'ZOOMIN': "zoomIn",
            'ZOOMINSLOW': "zoomInSlow",
            'ZOOMINFAST': "zoomInFast",
            'ZOOMOUT': "zoomOut",
            'ZOOMOUTSLOW': "zoomOutSlow",
            'ZOOMOUTFAST': "zoomOutFast",
            'SLIDELEFT': "slideLeft",
            'SLIDELEFTSLOW': "slideLeftSLow",
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
        },
        ('filter',): {
            'BOOST': "boost",
            'CONTRAST': "contrast",
            'DARKEN': "darken",
            'GREYSCALE': "greyscale",
            'LIGHTEN': "lighten",
            'MUTED': "muted",
            'NEGATIVE': "negative",
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
            'asset': (Asset,),  # noqa: E501
            'start': (float,),  # noqa: E501
            'length': (float,),  # noqa: E501
            'fit': (str,),  # noqa: E501
            'scale': (float,),  # noqa: E501
            'position': (str,),  # noqa: E501
            'offset': (Offset,),  # noqa: E501
            'transition': (Transition,),  # noqa: E501
            'effect': (str,),  # noqa: E501
            'filter': (str,),  # noqa: E501
            'opacity': (float,),  # noqa: E501
            'transform': (Transformation,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'asset': 'asset',  # noqa: E501
        'start': 'start',  # noqa: E501
        'length': 'length',  # noqa: E501
        'fit': 'fit',  # noqa: E501
        'scale': 'scale',  # noqa: E501
        'position': 'position',  # noqa: E501
        'offset': 'offset',  # noqa: E501
        'transition': 'transition',  # noqa: E501
        'effect': 'effect',  # noqa: E501
        'filter': 'filter',  # noqa: E501
        'opacity': 'opacity',  # noqa: E501
        'transform': 'transform',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, asset, start, length, *args, **kwargs):  # noqa: E501
        """Clip - a model defined in OpenAPI

        Args:
            asset (Asset):
            start (float): The start position of the Clip on the timeline, in seconds.
            length (float): The length, in seconds, the Clip should play for.

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
            fit (str): Set how the asset should be scaled to fit the viewport using one of the following options:    <ul>     <li>`crop` <b>(default)</b> - scale the asset to fill the viewport while maintaining the aspect ratio. The asset will be cropped if it exceeds the bounds of the viewport.</li>     <li>`cover` - stretch the asset to fill the viewport without maintaining the aspect ratio.</li>     <li>`contain` - fit the entire asset within the viewport while maintaining the original aspect ratio.</li>     <li>`none` - preserves the original asset dimensions and does not apply any scaling.</li>   </ul>. [optional]  # noqa: E501
            scale (float): Scale the asset to a fraction of the viewport size - i.e. setting the scale to 0.5 will scale asset to half the size of the viewport. This is useful for picture-in-picture video and  scaling images such as logos and watermarks.. [optional]  # noqa: E501
            position (str): Place the asset in one of nine predefined positions of the viewport. This is most effective for when the asset is scaled and you want to position the element to a specific position. <ul>   <li>`top` - top (center)</li>   <li>`topRight` - top right</li>   <li>`right` - right (center)</li>   <li>`bottomRight` - bottom right</li>   <li>`bottom` - bottom (center)</li>   <li>`bottomLeft` - bottom left</li>   <li>`left` - left (center)</li>   <li>`topLeft` - top left</li>   <li>`center` - center</li> </ul>. [optional]  # noqa: E501
            offset (Offset): [optional]  # noqa: E501
            transition (Transition): [optional]  # noqa: E501
            effect (str): A motion effect to apply to the Clip. <ul>   <li>`zoomIn` - slow zoom in</li>   <li>`zoomOut` - slow zoom out</li>   <li>`slideLeft` - slow slide (pan) left</li>   <li>`slideRight` - slow slide (pan) right</li>   <li>`slideUp` - slow slide (pan) up</li>   <li>`slideDown` - slow slide (pan) down</li> </ul> The motion effect speed can also be controlled by appending `Fast` or `Slow` to the effect, e.g. `zoomInFast` or `slideRightSlow`.. [optional]  # noqa: E501
            filter (str): A filter effect to apply to the Clip. <ul>   <li>`boost` - boost contrast and saturation</li>   <li>`contrast` - increase contrast</li>   <li>`darken` - darken the scene</li>   <li>`greyscale` - remove colour</li>   <li>`lighten` - lighten the scene</li>   <li>`muted` - reduce saturation and contrast</li>   <li>`negative` - negative colors</li> </ul>. [optional]  # noqa: E501
            opacity (float): Sets the opacity of the Clip where 1 is opaque and 0 is transparent.. [optional]  # noqa: E501
            transform (Transformation): [optional]  # noqa: E501
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

        self.asset = asset
        self.start = start
        self.length = length
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
    def __init__(self, asset, start, length, *args, **kwargs):  # noqa: E501
        """Clip - a model defined in OpenAPI

        Args:
            asset (Asset):
            start (float): The start position of the Clip on the timeline, in seconds.
            length (float): The length, in seconds, the Clip should play for.

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
            fit (str): Set how the asset should be scaled to fit the viewport using one of the following options:    <ul>     <li>`crop` <b>(default)</b> - scale the asset to fill the viewport while maintaining the aspect ratio. The asset will be cropped if it exceeds the bounds of the viewport.</li>     <li>`cover` - stretch the asset to fill the viewport without maintaining the aspect ratio.</li>     <li>`contain` - fit the entire asset within the viewport while maintaining the original aspect ratio.</li>     <li>`none` - preserves the original asset dimensions and does not apply any scaling.</li>   </ul>. [optional]  # noqa: E501
            scale (float): Scale the asset to a fraction of the viewport size - i.e. setting the scale to 0.5 will scale asset to half the size of the viewport. This is useful for picture-in-picture video and  scaling images such as logos and watermarks.. [optional]  # noqa: E501
            position (str): Place the asset in one of nine predefined positions of the viewport. This is most effective for when the asset is scaled and you want to position the element to a specific position. <ul>   <li>`top` - top (center)</li>   <li>`topRight` - top right</li>   <li>`right` - right (center)</li>   <li>`bottomRight` - bottom right</li>   <li>`bottom` - bottom (center)</li>   <li>`bottomLeft` - bottom left</li>   <li>`left` - left (center)</li>   <li>`topLeft` - top left</li>   <li>`center` - center</li> </ul>. [optional]  # noqa: E501
            offset (Offset): [optional]  # noqa: E501
            transition (Transition): [optional]  # noqa: E501
            effect (str): A motion effect to apply to the Clip. <ul>   <li>`zoomIn` - slow zoom in</li>   <li>`zoomOut` - slow zoom out</li>   <li>`slideLeft` - slow slide (pan) left</li>   <li>`slideRight` - slow slide (pan) right</li>   <li>`slideUp` - slow slide (pan) up</li>   <li>`slideDown` - slow slide (pan) down</li> </ul> The motion effect speed can also be controlled by appending `Fast` or `Slow` to the effect, e.g. `zoomInFast` or `slideRightSlow`.. [optional]  # noqa: E501
            filter (str): A filter effect to apply to the Clip. <ul>   <li>`boost` - boost contrast and saturation</li>   <li>`contrast` - increase contrast</li>   <li>`darken` - darken the scene</li>   <li>`greyscale` - remove colour</li>   <li>`lighten` - lighten the scene</li>   <li>`muted` - reduce saturation and contrast</li>   <li>`negative` - negative colors</li> </ul>. [optional]  # noqa: E501
            opacity (float): Sets the opacity of the Clip where 1 is opaque and 0 is transparent.. [optional]  # noqa: E501
            transform (Transformation): [optional]  # noqa: E501
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

        self.asset = asset
        self.start = start
        self.length = length
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
