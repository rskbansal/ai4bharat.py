from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'ai4bharat.py',
    version = '0.1.0',    
    description = 'An unofficial Python API wrapper for services provided by AI4Bharat.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/rskbansal/ai4bharat.py',
    author = 'Rhythm Bansal',
    author_email = 'rskbansal@outlook.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = [
        'requests',
        'soundfile',
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)