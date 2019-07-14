from setuptools import setup

setup(
    name='snek',
    entry_points={
        'console_scripts':[
            'snek = snek:main'
        ],
       'snek_types': [
           'normal = snek:normal_snek',
           'fancy = snek:fancy_snek',
       ],
    }
)