import setuptools
from distutils.dir_util import copy_tree
from pathlib import Path
PACKAGE_NAME='traffy'
MODULE_NAME='traffy'
import shutil, os
os.makedirs(os.path.dirname(PACKAGE_NAME + '/README.md'), exist_ok=True)
shutil.copy('README.md', PACKAGE_NAME + '/README.md')
def readme():
    with open('README.md', 'r') as fh:
        long_description = fh.read()
        return long_description

v = Path(MODULE_NAME + '/version').open(encoding = 'utf-8').read().splitlines()
setuptools.setup(
    name='traffy',
    version=v[0].strip(),
    author='Rahul Bhadani',
    author_email='rahulbhadani@email.arizona.edu',
    description='A package traffy.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/rahulbhadani/traffy',
    packages=setuptools.find_packages(),
    install_requires=[
        l.strip() for l in Path('requirements.txt').open(encoding = 'utf-8').read().splitlines()
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: AsyncIO',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        ],
    keywords='python',
    include_package_data=True,
    package_data={'traffy': ['README.md','version']},
    zip_safe=False
        )

os.remove('traffy/README.md')

