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


def lazy_import():
    from shotstack_sdk.model.hey_gen_text_to_avatar_options import HeyGenTextToAvatarOptions
    globals()['HeyGenTextToAvatarOptions'] = HeyGenTextToAvatarOptions


class HeyGenGeneratedAssetOptions(ModelComposed):
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
        ('type',): {
            'TEXT-TO-AVATAR': "text-to-avatar",
        },
        ('avatar_style',): {
            'NORMAL': "normal",
            'CIRCLE': "circle",
        },
        ('ratio',): {
            '16:9': "16:9",
            '9:16': "9:16",
        },
        ('avatar',): {
            'ANGELA': "Angela",
            'BILL': "Bill",
            'DAISY': "Daisy",
            'DEREK': "Derek",
            'EVA': "Eva",
            'JAKE': "Jake",
            'JEFF': "Jeff",
            'JEROME': "Jerome",
            'JOON': "Joon",
            'KAYLA': "Kayla",
            'KENT': "Kent",
            'LUNA': "Luna",
            'MARK': "Mark",
            'MATTHEW': "Matthew",
            'MONICA': "Monica",
            'PETER': "Peter",
            'SELINA': "Selina",
            'TANYA': "Tanya",
            'THOMAS': "Thomas",
            'TINA': "Tina",
            'TYLER': "Tyler",
            'VANESSA': "Vanessa",
            'VERA': "Vera",
            'WILSON': "Wilson",
            'ZOEY': "Zoey",
        },
        ('voice',): {
            'ABBI_-_NATURAL': "Abbi - Natural",
            'ADAM_-_NATURAL': "Adam - Natural",
            'AISTON_-_FRIENDLY': "Aiston - Friendly",
            'ALICE_-_NEWSCASTER': "Alice - Newscaster",
            'ALISON_-_CHEERFUL': "Alison - Cheerful",
            'AMBER_-_FRIENDLY': "Amber - Friendly",
            'AMY_-_WARM': "Amy - Warm",
            'ANA_-_CHEERFUL': "Ana - Cheerful",
            'ANTONI_-_FRIENDLY': "Antoni - Friendly",
            'ARIA_-_NEWSCASTER': "Aria - Newscaster",
            'ARNOLD_-_CHEERFUL': "Arnold - Cheerful",
            'ARTHUR_-_NATURAL': "Arthur - Natural",
            'BELLA_-_FRIENDLY': "Bella - Friendly",
            'BELLE_-_NATURAL': "Belle - Natural",
            'BRANDON_-_WARM': "Brandon - Warm",
            'BRIAN_-_NATURAL': "Brian - Natural",
            'BRUCE_-_NATURAL': "Bruce - Natural",
            'CERISE_-_CHEERFUL': "Cerise - Cheerful",
            'CHRISTOPHER_-_CALM': "Christopher - Calm",
            'CLARA_-_PROFESSIONAL': "Clara - Professional",
            'CONNOR_-_NATURAL': "Connor - Natural",
            'DAHLIA_-_FRIENDLY': "Dahlia - Friendly",
            'DAVIS_-_PROFESSIONAL': "Davis - Professional",
            'DEAN_-_NATURAL': "Dean - Natural",
            'DELBERT_-_CHEERFUL': "Delbert - Cheerful",
            'EDWARD_-_FRIENDLY': "Edward - Friendly",
            'ELAINE_-_CALM': "Elaine - Calm",
            'EMILY_-_NATURAL': "Emily - Natural",
            'EMMA_-_NEWSCASTER': "Emma - Newscaster",
            'ERIC_-_NEWSCASTER': "Eric - Newscaster",
            'GRACE_-_NATURAL': "Grace - Natural",
            'HAILEY_-_CALM': "Hailey - Calm",
            'INDIRA_-_CHEERFUL': "Indira - Cheerful",
            'ISABELLA_-_CHEERFUL': "Isabella - Cheerful",
            'JACOB_-_NATURAL': "Jacob - Natural",
            'JAHMAI_-_FRIENDLY': "Jahmai - Friendly",
            'JANE_-_SERIOUS': "Jane - Serious",
            'JASON_-_SERIOUS': "Jason - Serious",
            'JELLE_-_FRIENDLY': "Jelle - Friendly",
            'JEN_-_NATURAL': "Jen - Natural",
            'JENNY_-_PROFESSIONAL': "Jenny - Professional",
            'JODI_-_CHEERFUL': "Jodi - Cheerful",
            'JOEY_-_CALM': "Joey - Calm",
            'JOHAN_-_FRIENDLY': "Johan - Friendly",
            'JOSIE_-_CHEERFUL': "Josie - Cheerful",
            'KEANAN_-_NATURAL': "Keanan - Natural",
            'KEITH_-_CHEERFUL': "Keith - Cheerful",
            'KELLIE_-_FRIENDLY': "Kellie - Friendly",
            'LAUREN_-_FRIENDLY': "Lauren - Friendly",
            'LEAH_-_NATURAL': "Leah - Natural",
            'LIAM_-_PROFESSIONAL': "Liam - Professional",
            'LIBBY_-_NATURAL': "Libby - Natural",
            'LILY_-_PROFESSIONAL': "Lily - Professional",
            'LUCAS_-_NATURAL': "Lucas - Natural",
            'LUKE_-_PROFESSIONAL': "Luke - Professional",
            'LUNA_-_NATURAL': "Luna - Natural",
            'MARIEKE_-_NATURAL': "Marieke - Natural",
            'MATTHEW_-_PROFESSIONAL': "Matthew - Professional",
            'MICHELLE_-_NATURAL': "Michelle - Natural",
            'MITCHELL_-_NATURAL': "Mitchell - Natural",
            'MOLLY_-_NEWSCASTER': "Molly - Newscaster",
            'MONICA_-_CALM': "Monica - Calm",
            'NATASHA_-_PROFESSIONAL': "Natasha - Professional",
            'NEERJA_-_NEWSCASTER': "Neerja - Newscaster",
            'NOAH_-_SERIOUS': "Noah - Serious",
            'OLIVER_-_NEWSCASTER': "Oliver - Newscaster",
            'OLIVIA_-_CALM': "Olivia - Calm",
            'PAUL_-_NATURAL': "Paul - Natural",
            'PRABHAT_-_NATURAL': "Prabhat - Natural",
            'RAVEENA_-_NATURAL': "Raveena - Natural",
            'RUDI_-_FRIENDLY': "Rudi - Friendly",
            'RYAN_-_PROFESSIONAL': "Ryan - Professional",
            'SAM_-_NATURAL': "Sam - Natural",
            'SARA_-_CHEERFUL': "Sara - Cheerful",
            'SHERRY_-_FRIENDLY': "Sherry - Friendly",
            'SONIA_-_WARM': "Sonia - Warm",
            'THOMAS_-_NATURAL': "Thomas - Natural",
            'TODD_-_PROFESSIONAL': "Todd - Professional",
            'TONY_-_PROFESSIONAL': "Tony - Professional",
            'TRACY_-_CHEERFUL': "Tracy - Cheerful",
            'WAYNE_-_NATURAL': "Wayne - Natural",
            'WILDER_-_NATURAL': "Wilder - Natural",
            'WILLE_-_NATURAL': "Wille - Natural",
            'WILLIAM_-_FRIENDLY': "William - Friendly",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'type': (str,),  # noqa: E501
            'avatar_style': (str,),  # noqa: E501
            'background': (str,),  # noqa: E501
            'ratio': (str,),  # noqa: E501
            'test': (bool,),  # noqa: E501
            'text': (str,),  # noqa: E501
            'avatar': (str,),  # noqa: E501
            'voice': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'HeyGenTextToAvatarOptions': HeyGenTextToAvatarOptions,
            'text-to-avatar': HeyGenTextToAvatarOptions,
        }
        if not val:
            return None
        return {'type': val}

    attribute_map = {
        'type': 'type',  # noqa: E501
        'avatar_style': 'avatarStyle',  # noqa: E501
        'background': 'background',  # noqa: E501
        'ratio': 'ratio',  # noqa: E501
        'test': 'test',  # noqa: E501
        'text': 'text',  # noqa: E501
        'avatar': 'avatar',  # noqa: E501
        'voice': 'voice',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HeyGenGeneratedAssetOptions - a model defined in OpenAPI

        Keyword Args:
            type (str): The type of asset to generate - set to `text-to-avatar` for text-to-avatar.. defaults to "text-to-avatar", must be one of ["text-to-avatar", ]  # noqa: E501
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
            avatar_style (str): The display style of the avatar, a rectangle `normal` or circular `circle` background. Defaults to `normal`.. [optional]  # noqa: E501
            background (str): The background color of the video. Defaults to `#ffffff`.. [optional]  # noqa: E501
            ratio (str): The aspect ratio of the video, `16:9` horizontal or `9:16` vertical. Defaults to `16:9`.. [optional]  # noqa: E501
            test (bool): A boolean flag indicating whether the video is for testing purposes. See the \"test\" parameter in [HeyGen](https://docs.heygen.com/reference/generate-video) for more details.. [optional]  # noqa: E501
            text (str): The text or script that the avatar will narrate.. [optional]  # noqa: E501
            avatar (str): The avatar character to generate. Select from the list of available avatars: <ul>   <li>`Angela`</li>   <li>`Bill`</li>   <li>`Daisy`</li>   <li>`Derek`</li>   <li>`Eva`</li>   <li>`Jake`</li>   <li>`Jeff`</li>   <li>`Jerome`</li>   <li>`Joon`</li>   <li>`Kayla`</li>   <li>`Kent`</li>   <li>`Luna`</li>   <li>`Mark`</li>   <li>`Matthew`</li>   <li>`Monica`</li>   <li>`Peter`</li>   <li>`Selina`</li>   <li>`Tanya`</li>   <li>`Thomas`</li>   <li>`Tina`</li>   <li>`Tyler`</li>   <li>`Vanessa`</li>   <li>`Vera`</li>   <li>`Wilson`</li>   <li>`Zoey`</li> </ul>. [optional]  # noqa: E501
            voice (str): The avatars voice and speaking style. Select from the list of available voices: <ul>   <li>`Abb- - Natural`</li>   <li>`Adam - Natural`</li>   <li>`Aiston - Friendly`</li>   <li>`Alice - Newscaster`</li>   <li>`Alison - Cheerful`</li>   <li>`Amber - Friendly`</li>   <li>`Amy - Warm`</li>   <li>`Ana - Cheerful`</li>   <li>`Antoni - Friendly`</li>   <li>`Aria - Newscaster`</li>   <li>`Arnold - Cheerful`</li>   <li>`Arthur - Natural`</li>   <li>`Bella - Friendly`</li>   <li>`Belle - Natural`</li>   <li>`Brandon - Warm`</li>   <li>`Brian - Natural`</li>   <li>`Bruce - Natural`</li>   <li>`Cerise - Cheerful`</li>   <li>`Christopher - Calm`</li>   <li>`Clara - Professional`</li>   <li>`Connor - Natural`</li>   <li>`Dahlia - Friendly`</li>   <li>`Davis - Professional`</li>   <li>`Dean - Natural`</li>   <li>`Delbert - Cheerful`</li>   <li>`Edward - Friendly`</li>   <li>`Elaine - Calm`</li>   <li>`Emily - Natural`</li>   <li>`Emma - Newscaster`</li>   <li>`Eric - Newscaster`</li>   <li>`Grace - Natural`</li>   <li>`Hailey - Calm`</li>   <li>`Indira - Cheerful`</li>   <li>`Isabella - Cheerful`</li>   <li>`Jacob - Natural`</li>   <li>`Jahmai - Friendly`</li>   <li>`Jane - Serious`</li>   <li>`Jason - Serious`</li>   <li>`Jelle - Friendly`</li>   <li>`Jen - Natural`</li>   <li>`Jenny - Professional`</li>   <li>`Jodi - Cheerful`</li>   <li>`Joey - Calm`</li>   <li>`Johan - Friendly`</li>   <li>`Josie - Cheerful`</li>   <li>`Keanan - Natural`</li>   <li>`Keith - Cheerful`</li>   <li>`Kellie - Friendly`</li>   <li>`Lauren - Friendly`</li>   <li>`Leah - Natural`</li>   <li>`Liam - Professional`</li>   <li>`Libby - Natural`</li>   <li>`Lily - Professional`</li>   <li>`Lucas - Natural`</li>   <li>`Luke - Professional`</li>   <li>`Luna - Natural`</li>   <li>`Marieke - Natural`</li>   <li>`Matthew - Professional`</li>   <li>`Michelle - Natural`</li>   <li>`Mitchell - Natural`</li>   <li>`Molly - Newscaster`</li>   <li>`Monica - Calm`</li>   <li>`Natasha - Professional`</li>   <li>`Neerja - Newscaster`</li>   <li>`Noah - Serious`</li>   <li>`Oliver - Newscaster`</li>   <li>`Olivia - Calm`</li>   <li>`Paul - Natural`</li>   <li>`Prabhat - Natural`</li>   <li>`Raveena - Natural`</li>   <li>`Rudi - Friendly`</li>   <li>`Ryan - Professional`</li>   <li>`Sam - Natural`</li>   <li>`Sara - Cheerful`</li>   <li>`Sherry - Friendly`</li>   <li>`Sonia - Warm`</li>   <li>`Thomas - Natural`</li>   <li>`Todd - Professional`</li>   <li>`Tony - Professional`</li>   <li>`Tracy - Cheerful`</li>   <li>`Wayne - Natural`</li>   <li>`Wilder - Natural`</li>   <li>`Wille - Natural`</li>   <li>`William - Friendly`</li> </ul>. [optional]  # noqa: E501
        """

        type = kwargs.get('type', "text-to-avatar")
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HeyGenGeneratedAssetOptions - a model defined in OpenAPI

        Keyword Args:
            type (str): The type of asset to generate - set to `text-to-avatar` for text-to-avatar.. defaults to "text-to-avatar", must be one of ["text-to-avatar", ]  # noqa: E501
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
            avatar_style (str): The display style of the avatar, a rectangle `normal` or circular `circle` background. Defaults to `normal`.. [optional]  # noqa: E501
            background (str): The background color of the video. Defaults to `#ffffff`.. [optional]  # noqa: E501
            ratio (str): The aspect ratio of the video, `16:9` horizontal or `9:16` vertical. Defaults to `16:9`.. [optional]  # noqa: E501
            test (bool): A boolean flag indicating whether the video is for testing purposes. See the \"test\" parameter in [HeyGen](https://docs.heygen.com/reference/generate-video) for more details.. [optional]  # noqa: E501
            text (str): The text or script that the avatar will narrate.. [optional]  # noqa: E501
            avatar (str): The avatar character to generate. Select from the list of available avatars: <ul>   <li>`Angela`</li>   <li>`Bill`</li>   <li>`Daisy`</li>   <li>`Derek`</li>   <li>`Eva`</li>   <li>`Jake`</li>   <li>`Jeff`</li>   <li>`Jerome`</li>   <li>`Joon`</li>   <li>`Kayla`</li>   <li>`Kent`</li>   <li>`Luna`</li>   <li>`Mark`</li>   <li>`Matthew`</li>   <li>`Monica`</li>   <li>`Peter`</li>   <li>`Selina`</li>   <li>`Tanya`</li>   <li>`Thomas`</li>   <li>`Tina`</li>   <li>`Tyler`</li>   <li>`Vanessa`</li>   <li>`Vera`</li>   <li>`Wilson`</li>   <li>`Zoey`</li> </ul>. [optional]  # noqa: E501
            voice (str): The avatars voice and speaking style. Select from the list of available voices: <ul>   <li>`Abb- - Natural`</li>   <li>`Adam - Natural`</li>   <li>`Aiston - Friendly`</li>   <li>`Alice - Newscaster`</li>   <li>`Alison - Cheerful`</li>   <li>`Amber - Friendly`</li>   <li>`Amy - Warm`</li>   <li>`Ana - Cheerful`</li>   <li>`Antoni - Friendly`</li>   <li>`Aria - Newscaster`</li>   <li>`Arnold - Cheerful`</li>   <li>`Arthur - Natural`</li>   <li>`Bella - Friendly`</li>   <li>`Belle - Natural`</li>   <li>`Brandon - Warm`</li>   <li>`Brian - Natural`</li>   <li>`Bruce - Natural`</li>   <li>`Cerise - Cheerful`</li>   <li>`Christopher - Calm`</li>   <li>`Clara - Professional`</li>   <li>`Connor - Natural`</li>   <li>`Dahlia - Friendly`</li>   <li>`Davis - Professional`</li>   <li>`Dean - Natural`</li>   <li>`Delbert - Cheerful`</li>   <li>`Edward - Friendly`</li>   <li>`Elaine - Calm`</li>   <li>`Emily - Natural`</li>   <li>`Emma - Newscaster`</li>   <li>`Eric - Newscaster`</li>   <li>`Grace - Natural`</li>   <li>`Hailey - Calm`</li>   <li>`Indira - Cheerful`</li>   <li>`Isabella - Cheerful`</li>   <li>`Jacob - Natural`</li>   <li>`Jahmai - Friendly`</li>   <li>`Jane - Serious`</li>   <li>`Jason - Serious`</li>   <li>`Jelle - Friendly`</li>   <li>`Jen - Natural`</li>   <li>`Jenny - Professional`</li>   <li>`Jodi - Cheerful`</li>   <li>`Joey - Calm`</li>   <li>`Johan - Friendly`</li>   <li>`Josie - Cheerful`</li>   <li>`Keanan - Natural`</li>   <li>`Keith - Cheerful`</li>   <li>`Kellie - Friendly`</li>   <li>`Lauren - Friendly`</li>   <li>`Leah - Natural`</li>   <li>`Liam - Professional`</li>   <li>`Libby - Natural`</li>   <li>`Lily - Professional`</li>   <li>`Lucas - Natural`</li>   <li>`Luke - Professional`</li>   <li>`Luna - Natural`</li>   <li>`Marieke - Natural`</li>   <li>`Matthew - Professional`</li>   <li>`Michelle - Natural`</li>   <li>`Mitchell - Natural`</li>   <li>`Molly - Newscaster`</li>   <li>`Monica - Calm`</li>   <li>`Natasha - Professional`</li>   <li>`Neerja - Newscaster`</li>   <li>`Noah - Serious`</li>   <li>`Oliver - Newscaster`</li>   <li>`Olivia - Calm`</li>   <li>`Paul - Natural`</li>   <li>`Prabhat - Natural`</li>   <li>`Raveena - Natural`</li>   <li>`Rudi - Friendly`</li>   <li>`Ryan - Professional`</li>   <li>`Sam - Natural`</li>   <li>`Sara - Cheerful`</li>   <li>`Sherry - Friendly`</li>   <li>`Sonia - Warm`</li>   <li>`Thomas - Natural`</li>   <li>`Todd - Professional`</li>   <li>`Tony - Professional`</li>   <li>`Tracy - Cheerful`</li>   <li>`Wayne - Natural`</li>   <li>`Wilder - Natural`</li>   <li>`Wille - Natural`</li>   <li>`William - Friendly`</li> </ul>. [optional]  # noqa: E501
        """

        type = kwargs.get('type', "text-to-avatar")
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              HeyGenTextToAvatarOptions,
          ],
        }