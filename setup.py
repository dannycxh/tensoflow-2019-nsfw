# coding=utf-8

from distutils.core import setup

setup(
    # Application name:
    name="tensor-nsfw",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Danny",
    author_email="dannycxh@gmail.com",

    # Packages
    packages=[
        "face","model","nsfw","util",
    ],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://github.com/SendingIO/tensor-nsfw",
    license="LICENSE",
    description="Danny testing.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        'requests',
        'opencv-python'
    ],

    extras_require={
        'tensorflow_export': ["tensorflow"],
    }
)