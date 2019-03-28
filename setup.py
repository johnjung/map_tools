import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='iiif_tools',
    version='0.0.1',
    author='John Jung',
    author_email='jej@uchicago.edu',
    description='Scripts to build IIIF records for digital collections at the University of Chicago.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/johnjung/iiif_tools',
    packages=setuptools.find_packages()
)
