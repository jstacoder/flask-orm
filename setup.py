from setuptools import setup

setup(
    name="flask-orm",
    version="0.0.1",
    packages=['flask_orm'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'SQLAlchemy'],
    include_package_data=True,
)
