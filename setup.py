from setuptools import find_packages, setup

from wagtailextraicons import __version__

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='wagtailextraicons',
    version=__version__,
    description='Add extra icons to your Wagtail project.',
    long_description=long_description,
    url='https://github.com/octavenz/wagtailextraicons',
    author='Sam Costigan (Octave)',
    author_email='sam@octave.nz',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.1',
        'wagtail>=2.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management'
    ]

)
