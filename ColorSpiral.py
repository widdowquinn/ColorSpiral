"""ColorSpiral.py

Generate RGB colours suitable for distinguishing categorical data.

This module provides a class that implements a spiral 'path' through HSV
colour space, permitting the selection of a number of points along that path,
and returning the output in RGB colour space, suitable for use with ReportLab
and other graphics packages.

This approach to colour choice was inspired by Bang Wong's Points of View
article: Color Coding, in Nature Methods _7_ 573 (doi:10.1038/nmeth0810-573).

The module also provides helper functions that return a list for colours, or
a dictionary of colours (if passed an iterable containing the names of
categories to be coloured).

(c) The James Hutton Institute 2013
Author: Leighton Pritchard

Contact:
leighton.pritchard@hutton.ac.uk

Leighton Pritchard,
Information and Computing Sciences,
James Hutton Institute,
Errol Road,
Invergowrie,
Dundee,
DD6 9LH,
Scotland,
UK

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# standard library
import cmath       # polar <-> Cartesian conversions
import colorsys    # colour format conversions
from math import log, exp, floor, pi
import random      # for jitter values


class ColorSpiral(object):
    """Implement a spiral path through HSV colour space.

       This class provides functions for sampling points along a logarithmic
       spiral path through HSV colour space.

       The spiral is described by r = a * exp(b * t) where r is the distance
       from the axis of the HSV cylinder to the current point in the spiral,
       and t is the angle through which the spiral has turned to reach the
       current point. a and b are (positive, real) parameters that control the
       shape of the spiral.

       a: the starting direction of the spiral
       b: the number of revolutions about the axis made by the spiral

       We permit the spiral to move along the cylinder ('in V-space') between
       v_init and v_final, to give a gradation in V (essentially, brightness),
       along the path, where v_init, v_final are in [0,1].

       A brightness 'jitter' may also be provided as an absolute value in
       V-space, to aid in distinguishing consecutive colour points on the
       path.
    """
    def __init__(self, a=1, b=0.33, v_init=0.85, v_final=0.5,
                 jitter=0.05):
        """Initialise a logarithmic spiral path through HSV colour space

           Arguments:

           o a - Parameter a for the spiral, controls the initial spiral
                 direction. a > 0

           o b - parameter b for the spiral, controls the rate at which the
                 spiral revolves around the axis. b > 0

           o v_init - initial value of V (brightness) for the spiral.
                      v_init in [0,1]

           o v_final - final value of V (brightness) for the spiral
                      v_final in [0,1]

           o jitter - the degree of V (brightness) jitter to add to each
                      selected colour. The amount of jitter will be selected
                      from a uniform random distribution [-jitter, jitter],
                      and V will be maintained in [0,1].
        """
        # Initialise attributes
        self.a = a
        self.b = b
        self.v_init = v_init
        self.v_final = v_final
        self.jitter = jitter

    def get_colors(self, k, offset=0.1):
        """ A generator returning the RGB colour space values for k
            evenly-spaced points along the defined spiral in HSV space.

            Arguments:

            o k - the number of points to return

            o offset - how far along the spiral path to start.
        """
        # We use the offset to skip a number of similar colours near to
        # HSV axis
        assert offset > 0 and offset < 1, "offset must be in (0,1)"
        v_rate = (self._v_final - self._v_init) / float(k)
        # Generator for colours: we have divided the arc length into sections
        # of equal length, and step along them
        for n in range(1, k+1):
            # For each value of n, t indicates the angle through which the
            # spiral has turned, to this point
            t = (1./self._b) * (log(n + (k * offset)) -
                                log((1 + offset) * k * self._a))
            # Put 0 <= h <= 2*pi, where h is the angular part of the polar
            # co-ordinates for this point on the spiral
            h = t
            while h < 0:
                h += 2 * pi
            h = (h - (floor(h/(2 * pi)) * pi))
            # Now put h in [0, 1] for colorsys conversion
            h = h / (2 * pi)
            # r is the radial distance of this point from the centre
            r = self._a * exp(self._b * t)
            # v is the brightness of this point, linearly interpolated
            # from self._v_init to self._v_final. Jitter size is sampled from
            # a uniform distribution
            if self._jitter:
                jitter = random.random() * 2 * self._jitter - self._jitter
            else:
                jitter = 0
            v = self._v_init + (n * v_rate + jitter)
            # We have arranged the arithmetic such that 0 <= r <= 1, so
            # we can use this value directly as s in HSV
            yield colorsys.hsv_to_rgb(h, r, max(0, min(v, 1)))

    def get_a(self):
        return self._a

    def set_a(self, value):
        self._a = max(0, value)

    def get_b(self):
        return self._b

    def set_b(self, value):
        self._b = max(0, value)

    def get_v_init(self):
        return self._v_init

    def set_v_init(self, value):
        self._v_init = max(0, min(1, value))

    def get_v_final(self):
        return self._v_final

    def set_v_final(self, value):
        self._v_final = max(0, min(1, value))

    def get_jitter(self):
        return self._jitter

    def set_jitter(self, value):
        self._jitter = max(0, min(1, value))

    a = property(get_a, set_a)
    b = property(get_b, set_b)
    v_init = property(get_v_init, set_v_init)
    v_final = property(get_jitter, set_v_final)
    jitter = property(get_jitter, set_jitter)


# Convenience functions for those who don't want to bother with a
# ColorSpiral object
def get_colors(k, **kwargs):
    """Returns k colours selected by the ColorSpiral object, as a generator

       Arguments:

       o k - the number of colours to return

       o **kwargs - pass-through arguments to the ColorSpiral object
    """
    cs = ColorSpiral(**kwargs)
    return cs.get_colors(k)


def get_color_dict(l, **kwargs):
    """Returns a dictionary, keyed by the members of iterable l, with a
       colour assigned to each member.

       Arguments:

       o l - an iterable representing classes to be coloured

       o **kwargs - pass-through arguments to the ColorSpiral object
    """
    cs = ColorSpiral(**kwargs)
    colors = cs.get_colors(len(l))
    dict = {}
    for item in l:
        dict[item] = colors.next()
    return dict
