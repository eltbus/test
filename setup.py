from setuptools import setup, find_packages

setup(
    name="guille-test",
    version="0.0.1",
    author="Guillermo Sanchez",
    author_email="naselliug@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["run = src.main:do_something"]},
)
