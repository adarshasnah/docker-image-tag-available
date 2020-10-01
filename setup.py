from setuptools import setup

setup(name='docker-image-tag-available',
    version='1.0',
    description='Command line tool check whether an image tag is already used',
    url='https://github.com/adarshasnah/docker-image-tag-available',
    author='Adarsh Hasnah',
    license='MIT',
    packages=['docker_image_tag_available'],
    zip_safe=False,
    install_requires=[
        'click',
        'requests'
    ],
    entry_points = {
        'console_scripts': ['docker-image-tag-available=docker_image_tag_available.cli:main'],
    }
)