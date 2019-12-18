import subprocess

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as base_sdist
from setuptools.command.bdist_egg import bdist_egg as base_bdist_egg

from wagtailextraicons import __version__


class assets_mixin:
    def compile_assets(self):
        try:
            subprocess.check_call(['npm', 'install'])
            subprocess.check_call(['npm', 'run', 'build'])
        except (OSError, subprocess.CalledProcessError) as e:
            print('Error compiling assets: ' + str(e))
            raise SystemExit(1)


class sdist(base_sdist, assets_mixin):
    def run(self):
        self.compile_assets()
        base_sdist.run(self)


class bdist_egg(base_bdist_egg, assets_mixin):
    def run(self):
        self.compile_assets()
        base_bdist_egg.run(self)


setup(
    version=__version__,
    cmdclass={
        'sdist': sdist,
        'bdist_egg': bdist_egg
    },
)
