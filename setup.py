import os
import io
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='pancli',
    version='0.0.1',
    author='kevenli',
    author_email='pbleester@gmail.com',
    url='https://github.com/pansihub/pancli',
    description='pansihub command-line tools.',
    entry_points={
        'console_scripts': [
            'pansi = pancli.cli:main',
            'pancli = pancli.cli:main',
        ]
    },
)
