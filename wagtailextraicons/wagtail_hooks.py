try:
    from wagtail import hooks
except ImportError:
    raise ImportError('wagtailextraicons requires Wagtail >= 3.0')

# Note: .icon_register.py is generated in the build task of this package
from .icon_register import icons as extra_icons


@hooks.register('register_icons')
def register_icons(icons):
    for icon in extra_icons:
        icons.append(f'extraicons/{icon}')
    return icons
