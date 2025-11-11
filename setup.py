from setuptools import setup, find_packages

setup(
    name="tallerjuangubio",
    version="0.1.0",
    description="A simple Flask app by JuanGubio",
    author="JuanGubio",
    author_email="juan@example.com",
    packages=find_packages(),
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "tallerjuangubio = app:main",
        ],
    },
)