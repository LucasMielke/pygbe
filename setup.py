from setuptools import setup

setup(
    name = 'pygbe',
    version = '0.1.0',
    author = 'Lucas Mielke',
    author_email = 'lucas.mielke@outlook.com',
    packages = ['pygbe'],
    description = 'pygbe is a library with functions to get data from IBGE (Brazilian Institute of Geography and Statistics) via API',
    long_description = 'pygbe is a library with functions to get data from IBGE (Brazilian Institute of Geography and Statistics) via API ',
    
    url = 'https://github.com/LucasMielke/pygbe',
    project_urls = {
        'Código fonte': 'https://github.com/LucasMielke/pygbe',
        'Download': 'https://github.com/LucasMielke/pygbe/archive/0.1.0.zip'
    },
    license = 'MIT',
    keywords = 'Pesquisa Agrícola Municipal (PAM) from IBGE',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Other/Nonlisted Topic'
    ]
)