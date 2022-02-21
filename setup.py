import os
from bs4 import BeautifulSoup
import glob


from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as base_sdist
from setuptools.command.bdist_egg import bdist_egg as base_bdist_egg

from wagtailextraicons import __version__


url = 'https://github.com/octavenz/wagtailextraicons'
icon_src_dir = 'lib/icons'


class IconsDocMixin:
    def build_icons_doc(self):
        extraicons = os.listdir(icon_src_dir)

        with open('docs/icons.md', 'w') as file:
            file.write('| Icon | Name |\n')
            file.write('| --- | --- |\n')
            for icon_file in sorted(extraicons):
                icon_name = icon_file.split('.')[0]
                icon_image_url = '{0}/blob/master/{1}/{2}'.format(url, icon_src_dir, icon_file)
                file.write(
                    '| ![{name}]({url}) | {name} |\n'.format(name=icon_name, url=icon_image_url)
                )


class IconRegisterMixin:
    icon_register = []
    icon_paths = []
    icon_dest_dir = 'wagtailextraicons/templates/extraicons'
    icon_register_path = 'wagtailextraicons/icon_register.py'

    def register_icons(self):
        self.icon_paths = glob.glob(f'{icon_src_dir}/*.svg')
        self.process_src_icons()
        self.write_icon_register_module()

    def process_src_icons(self):
        for icon_path in self.icon_paths:
            icon_file_name = os.path.basename(icon_path)
            icon_name = icon_file_name[0:-4]
            dest_name = f'extraicons--{icon_name}'
            dest_filename = f'extraicons--{icon_name}.svg'

            with open(icon_path) as fp:
                symbol = self.convert_svg_to_symbol(fp, dest_name)

                if symbol:
                    self.icon_register.append(dest_filename)
                    self.write_symbol_to_template(symbol, dest_filename)
                else:
                    print(f'No Svg Found - {icon_path}')

    @staticmethod
    def convert_svg_to_symbol(file_contents, name):
        soup = BeautifulSoup(file_contents, 'html.parser')
        svg = soup.find('svg')

        if svg:
            svg.name = 'symbol'
            svg.attrs = {
                'id': f'icon-{name}',
                'viewbox': svg['viewbox']
            }
            return svg

        return None

    def write_symbol_to_template(self, symbol, file_name):
        html = symbol.prettify("utf-8")

        with open(f"{self.icon_dest_dir}/{file_name}", "wb") as file:
            file.write(html)

    def write_icon_register_module(self):
        with open(self.icon_register_path, "w") as file:
            output = "# This file is generated. Don't edit directly\n"
            icons_str = ''

            for icon_name in self.icon_register:
                icons_str += f"\n    '{icon_name}', "

            output += f'icons = [{ icons_str }\n]\n'
            file.write(output)


class sdist(base_sdist, IconRegisterMixin, IconsDocMixin):
    def run(self):
        self.build_icons_doc()
        self.register_icons()
        base_sdist.run(self)


class bdist_egg(base_bdist_egg, IconRegisterMixin, IconsDocMixin):
    def run(self):
        self.build_icons_doc()
        self.register_icons()
        base_bdist_egg.run(self)


setup(
    url=url,
    version=__version__,
    cmdclass={
        'sdist': sdist,
        'bdist_egg': bdist_egg
    },
)
