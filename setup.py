from setuptools import setup, find_packages

setup(
    name="Hajime",
    version="1.0",
    packages=find_packages(),
    install_requires=['sqlalchemy-2.0.38'],  # Add dependencies here
    author="Franciszek Czajkowski",
    description="Lightweight Website Framework",
    url="https://github.com/yourusername/my_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)