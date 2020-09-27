from setuptools import setup, find_packages

setup(
    name='python-ubuntu',
    description='Installation på Kubuntu og Manjaro',
    version='0.1.0',
    license='MIT',
    author='Jackie B',
    author_email='brundtoe@outlook.dk',
    install_requires=[
        'requests == 2.24.0',
        'Jinja2 == 2.11.2',
        'Sphinx == 3.2.1',
        'sphinx-rtd-theme == 0.5.0'
    ],
    packages=find_packages(),
)
