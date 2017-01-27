from setuptools import setup

setup(
    name='cli_push',
    version='0.1.0',
    py_modules=['cli_push', 'push_service'],
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        cli_push = cli_push:cli_push
    '''
)