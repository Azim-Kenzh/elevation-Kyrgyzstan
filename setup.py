from setuptools import setup


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip to next iteration if comment or empty line
        if line.startswith('#') or line == '' or line.startswith('http') or line.startswith('git'):
            continue
        # add line to requirements
        requirements.append(line.replace('\n', ''))
    return requirements


setup(
    name='elevation-Kyrgyzstan',
    packages=['elevation'],
    version='0.0.1',
    description='Get the elevation of any ground point in Kyrgyzstan with Elevation-Kyrgyzstan',
    long_description=open("README.rst", "r").read(),
    include_package_data=True,
    package_data={'elevation': ['KG_ELEVATION/*.nc']},
    author='Azimkozho Kenzhebek uulu',
    author_email='azimkozho.inventor@gmail.com',
    url='https://github.com/Azim-Kenzh/elevation-Kyrgyzstan',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    install_requires=get_install_requires(),
)

