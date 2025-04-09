from setuptools import setup, find_packages

setup(
    name='contextbase-py',
    version='1.0.0',
    description='Python SDK for interacting with the ContextBase memory API.',
    author='Fenil Jikadara',
    url='https://github.com/imfeniljikadara/contextbase-py',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
