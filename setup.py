from setuptools import setup, find_packages
from rocket import __version__

setup(
    name='rocket',
    version=__version__,
    author='Breitburg',
    include_package_data=True,
    url='https://github.com/breitburg/rocket',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pysdl2',
        'reloadr'
    ],
    entry_points={
        'console_scripts': ['rocket=rocket.tool:command'],
    }
)
