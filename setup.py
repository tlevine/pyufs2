from setuptools import setup, find_packages

setup(
    name='ufs2',
    version='0.0.1',
    packages=find_packages(),

    install_requires=[
        'lxml'
    ],

    author='Randall Leeds and Tom Levine',
    maintainer='Randall Leeds',
    maintainer_email='randall.leeds@gmail.com',
    description='A microformats2 parser.',
    license='MIT License',
    keywords='microformats semanticweb',

    url='http://ufs.cc/',
    download_url='https://github.com/tlevine/pyufs2',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],

    include_package_data=True,
    zip_safe=False,
)
