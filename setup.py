from setuptools import find_packages, setup
from hiq import read_file


setup(
    name='minichatgpt',
    maintainer='Juncong Moo',
    version=read_file('version.txt',by_line=False),
    packages=find_packages(exclude=(
        'tests',
        'benchmarks',
        '*.egg-info',
    )),
    description='A RLFH implementation (ChatGPT) powered by ColossalAI',
    long_description=read_file('README.md',by_line=False),
    long_description_content_type='text/markdown',
    license='Apache Software License 2.0',
    url='https://github.com/hpcaitech/ChatGPT',
    install_requires=read_file('requirements.txt'),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Environment :: GPU :: NVIDIA CUDA',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: System :: Distributed Computing',
    ],
)
