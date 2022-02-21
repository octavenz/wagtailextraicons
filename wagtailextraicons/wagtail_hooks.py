from pkg_resources import parse_version

from wagtail import __version__ as WAGTAIL_VERSION
from wagtail.core import hooks

if parse_version(WAGTAIL_VERSION) <= parse_version('2.15'):
    raise Exception('wagtailextraicons 2 requires Wagtail > 2.15')

# Note: .icon_register.py is generated in the build task of this package
from .icon_register import icons

@hooks.register('register_icons')
def register_icons(_icons):
    for icon in icons:
        _icons.append("extraicons/{}".format(icon))
    return _icons
