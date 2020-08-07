from setuptools import setup


REQUIRES = ['marshmallow', 'marshmallow-dataclass', 'numpy']

with open('README.md', 'r') as f:
    readme = f.read()

if __name__ == '__main__':
    setup(
        name='marshmallow-numpy',
        version='0.3.0',
        author='Shachak Zicher',
        author_email='shachakz12@gmail.com',
        description='Marshmallow numpy field',
        long_description=f'{readme}\n',
        package_data={'': ['LICENSE', 'README.md']},
        include_package_data=True,
        license='MIT',
        packages=['marshmallow_numpy'],
        install_requires=REQUIRES,
        url='https://github.com/shachakz/marshmallow_numpy'
    )
