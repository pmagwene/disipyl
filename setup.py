# setup.py - disipyl setup file


from distutils.core import setup


LONGDESC = """\
disipyl is an object-oriented 2D and 3D plotting module for Python.
disipyl is based on the plotting library DISLIN."""


setup(  name="disipyl",
        version="0.9",
        description="2D and 3D Plotting for Python",
        long_description = LONGDESC,
        author="Paul Magwene",
        author_email="paul.magwene@duke.edu",
        license="GPL",
        package_dir={'disipyl':'.'},
        packages = ['disipyl','disipyl.optioninfo'],
        )
