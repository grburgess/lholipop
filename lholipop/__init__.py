# -*- coding: utf-8 -*-

"""Top-level package for lholipop."""

__author__ = """J. Michael Burgess"""
__email__ = 'jburgess@mpe.mpg.de'


from .utils.configuration import lholipop_config, show_configuration
from .utils.logging import update_logging_level, activate_warnings, silence_warnings

from . import _version
__version__ = _version.get_versions()['version']
