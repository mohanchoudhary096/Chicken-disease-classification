from setuptools import find_packages,setup

with open ("README.md", 'r',encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'
REPO_NAME="Chicken-disease-classification"
AUTHOR_USER_NAME='mohanchoudhary'
SRC_REPO='CnnClassifier'
AUTHOR_EMAIL='mohanchoudhary096@gmail.com'



setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for cnn app',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug tracker':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'

    },
    package_dir={"": "src"},
    packages=find_packages(where="src"))