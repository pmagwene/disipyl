disipyl
=======

disipyl is an object-oriented wrapper around the DISLIN plotting
library.  DISLIN is a powerful and flexible multiplatform (Win32,
Unix, Linux, etc.) library designed for displaying scientific data.
DISLIN's author, Helmut Michels, has made available a DISLIN plotting
extension for the Python programming language (see
http://www.linmpi.mpg.de/dislin/ for more details).

disipyl provides a set of classes which represent various aspects
of DISLIN plots, as well as providing some easy to use classes for
creating commonly used plot formats (e.g. scatter plots, histograms,
3-D surface plots).  A major goal in designing the library was to
facilitate interactive data exploration and plot creation.

Documentation, a tutorial, and a demo program are included. 

**IMPORTANT NOTE**: disipyl is no longer under active development, but a couple of times a year I get requests for the disipyl code base, so I decided to clean it up a bit and make it available on github.  I have confirmed that the posted code works with the latest version of DISLIN (10.3.3, as of June 2013). Unless you have a specific use case that requires the capabilities of DISLIN I recommend Matplotlib for your day-to-day Python plotting needs.