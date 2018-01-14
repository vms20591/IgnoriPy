from setuptools import setup, find_packages

setup(
    name='ignoripy',
    version='1.0.0',
    author='Meenakshi Sundaram',
    author_email='vms20591@gmail.com',
    url='https://github.com/vms20591/IgnoriPy',
    description='IgnoriPy is a script to quicky generate a `.gitignore` when starting new projects',
    license='GPL V3',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points="""
    [console_scripts]
    ignoripy=ignoripy.main:main
    """,
    python_requires='>=2.7',
    install_requires=["requests==2.18.4","future==0.16.0"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: GNU General Public License (GPL)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
      ]
)