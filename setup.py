from setuptools import setup

setup(
    name='feature_lib',
    url='https://github.com/miararoy/feature_lib',
    author='Roy Miara',
    author_email='miararoy@gmail.com',
    packages=[
        'etl_abc'
    ],
    install_requires=[
        'pandas==0.25.0'
    ],
    version='1.0',
    description='feature lib utils',
    long_description=open('README.md').read(),
)