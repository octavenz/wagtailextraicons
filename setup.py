import os
import subprocess

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as base_sdist
from setuptools.command.bdist_egg import bdist_egg as base_bdist_egg

from wagtailextraicons import __version__


url = 'https://github.com/octavenz/wagtailextraicons'
extraicons_dir = 'wagtailextraicons/static_src/wagtailextraicons/extraicons'


class icons_doc_mixin:
    def build_icons_doc(self):
        extraicons = os.listdir(extraicons_dir)

        with open('docs/icons.md', 'w') as file:
            file.write('| Icon | Name |\n')
            file.write('| --- | --- |\n')
            for icon_file in sorted(extraicons):
                icon_name = icon_file.split('.')[0]
                icon_image_url = '{0}/blob/master/{1}/{2}'.format(url, extraicons_dir, icon_file)
                file.write(
                    '| ![{name}]({url}) | {name} |\n'.format(name=icon_name, url=icon_image_url)
                )


class assets_mixin:
    def compile_assets(self):
        try:
            subprocess.check_call(['npm', 'install'])
            subprocess.check_call(['npm', 'run', 'build'])
        except (OSError, subprocess.CalledProcessError) as e:
            print('Error compiling assets: ' + str(e))
            raise SystemExit(1)


class sdist(base_sdist, assets_mixin, icons_doc_mixin):
    def run(self):
        self.build_icons_doc()
        self.compile_assets()
        base_sdist.run(self)


class bdist_egg(base_bdist_egg, assets_mixin, icons_doc_mixin):
    def run(self):
        self.build_icons_doc()
        self.compile_assets()
        base_bdist_egg.run(self)


setup(
    url=url,
    version=__version__,
    cmdclass={
        'sdist': sdist,
        'bdist_egg': bdist_egg
    },
)
