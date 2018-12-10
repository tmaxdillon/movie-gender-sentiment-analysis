import os
from setuptools import setup

# Get version and release info, which is all stored in shablona/version.py
ver_file = os.path.join('movie_analysis', 'version.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name="movie_analysis",
            description="finds correlation between gender diversity in a movie and overall sentiment of youtube trailer comments",        
            version='1.0',
            install_requires=['textblob','pytest','pandas']
            )


if __name__ == '__main__':
    setup(**opts)