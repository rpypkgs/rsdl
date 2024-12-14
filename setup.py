from distutils.core import setup


with open("README.txt") as f:
    readme = f.read()

setup(
    name="rsdl",
    description="A SDL library that works with RPython",
    long_description=readme,
    version="0.4.2",
    author="PyPy contributors",
    author_email="timfelgentreff+rsdl@gmail.com",
    url="https://bitbucket.org/pypy/rsdl/",
    packages=["rsdl", "rsdl.cocoapy"],
    data_files=[("macosx-sdl-main",
                 ["rsdl/macosx-sdl-main/SDLMain.h",
                  "rsdl/macosx-sdl-main/SDLMain.m"])]
)
