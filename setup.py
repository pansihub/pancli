import os
import io
from setuptools import setup, find_packages


setup(
    name='pancli',
    version='0.0.3',
    author='kevenli',
    author_email='pbleester@gmail.com',
    url='https://github.com/pansihub/pancli',
    packages=find_packages(),
    description='pansihub command-line tools.',
    entry_points={
        'console_scripts': [
            'pansi = pancli.cli:main',
            'pancli = pancli.cli:main',
        ]
    },
)
