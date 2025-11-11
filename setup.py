from setuptools import setup, find_packages

setup(
    name="tallerjuangubio",
    version="0.1.0",
    description="A simple package by JuanGubio",
    author="JuanGubio",
    author_email="juan@example.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tallerjuangubio = tallerjuangubio:hola",
        ],
    },
)