import setuptools

setuptools.setup(
    name="forexrateapi",
    version="1.1.2",
    url="https://github.com/forexrateapi/forexrateapi-python",

    license_files=('LICENSE'),

    author="ForexRateAPI",
    author_email="contact@forexrateapi.com",

    description="Official Python wrapper for forexrateapi.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.31.0'],
    keywords=['currency', 'foreign exchange rate', 'currency conversion', 'exchangerate', 'rates'],
)
