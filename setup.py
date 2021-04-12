from setuptools import setup

setup(
    name='pypi_searcher',
    version=0.6,
    packages=['pypi_searcher'],
    url='https://github.com/dkucic/PyPI_Search',
    download_url='https://github.com/dkucic/PyPI_Search/archive/refs/tags/0.1.tar.gz',
    license='MIT',
    author='Damir Kucic',
    author_email='dkucic@gmail.com',
    description='Search pypi for package name, description and number of monthly downloads.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)

