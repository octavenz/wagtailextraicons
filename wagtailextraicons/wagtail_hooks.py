from django.utils.html import format_html
from pkg_resources import parse_version

try:
    from django.templatetags.static import static
except ImportError:  # Fallback for Django <2.1
    from django.contrib.staticfiles.templatetags.staticfiles import static

try:
    from wagtail import __version__ as WAGTAIL_VERSION
    from wagtail.core import hooks
except ImportError:  # Fallback for Wagtal <2.0
    from wagtail.wagtailcore import __version__ as WAGTAIL_VERSION
    from wagtail.wagtailcore import hooks


def extraicons_stylesheet():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('wagtailextraicons/css/main.css')
    )


# New Wagtail versions support importing CSS throughout the admin.
# Fall back to the old hook (editor screen only) for older versions.
if parse_version(WAGTAIL_VERSION) >= parse_version('1.4'):
    admin_stylesheet_hook = 'insert_global_admin_css'
else:
    admin_stylesheet_hook = 'insert_editor_css'

hooks.register(admin_stylesheet_hook, extraicons_stylesheet)
