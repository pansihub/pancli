import os
from os.path import join, dirname
import io
from setuptools import setup, find_packages


with open(join(dirname(__file__), 'pancli/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()


setup(
    name='pancli',
    version=version,
    author='kevenli',
    author_email='pbleester@gmail.com',
    url='https://github.com/pansihub/pancli',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    description='pansihub command-line tools.',
    entry_points={
        'console_scripts': [
            'pansi = pancli.cli:main',
            'pancli = pancli.cli:main',
        ]
    },
)
