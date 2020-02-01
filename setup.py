from setuptools import setup,find_packages



setup(
    name='pathify',
    version='0.0.1',
    description="Map <key:path> for path with a key",
    py_modules=['workspace','wsp','emoji'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        wsp=workspace:cli
    ''',
)
