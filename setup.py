from setuptools import setup,find_packages
import pathlib


HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pathify',
    version='0.1.1',
    description="Map <key:path> for path with a key",
    url="https://github.com/burdier/pathify",
    author="Burdier",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=['workspace','wsp','emoji'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ptfy=workspace:cli
    ''',
)
