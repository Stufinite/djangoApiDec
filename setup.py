from distutils.core import setup

setup(
    name = 'djangoApiDec',
    packages = ['djangoApiDec'],
    version = '0.1',
    description = 'Convenient python decorator usually used for building api',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/Stufinite/djangoApiDec',
    download_url = 'download link you saved',
    keywords = ['tag1', 'tag2'],
    classifiers = [],
    license='MIT',
    install_requires=[
        'django==1.10.3',
        'requests',
        'simplejson'
    ],
)
