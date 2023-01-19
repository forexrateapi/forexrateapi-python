import setuptools

setuptools.setup(
    name="forexrateapi",
    version="1.0.3",
    url="https://github.com/forexrateapi/forexrateapi-python",

    author="ForexRateAPI",
    author_email="contact@forexrateapi.com",

    description="Official Python wrapper for forexrateapi.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.9.1'],
    keywords=['currency', 'foreign exchange rate', 'currency conversion', 'exchangerate', 'rates'],
)
