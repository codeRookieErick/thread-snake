import setuptools

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

setuptools.setup(    
    name="threadsnake",
    version="0.0.1",
    author="Erick Fernando Mora Ramirez",
    author_email="erickfernandomoraramirez@gmail.com",
    description="A tiny server-side express-like library",
    long_description=readfile("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/codeRookieErick/thread-snake",
    project_urls={
        "Bug Tracker": "https://dev.moradev.dev/threadsnake/issues/",
        "Documentation": "https://dev.moradev.dev/threadsnake/documentation/",
    },
    package_data={
        "":["*.txt"]
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)