#README.md - ColorSpiral.py

## Overview

`ColorSpiral.py` is code to define a spiral in HSV colour space, and select 
colours along that spiral. The idea is that such colours will be - for
small numbers of colours - particularly distinguishable from each other.
Where large numbers of colours are chosen, it can help to use a 
brightness jitter.

This code was eventually contributed to [`Biopython`](http://www.biopython.org) as `Bio.Graphics.ColorSpiral`, but was provided as an early release in this form to accompany a blog post at
[http://armchairbiology.blogspot.com/](http://armchairbiology.blogspot.com/).

## Usage

The test script `test_ColorSpiral.py` provides example usage and output.

1. A square with jittered colours
!["A square with jittered colours."](Graphics/square_test.pdf "A square with jittered colours.")

2. A spiral indicating the locations of the chosen colours in HSV space:
!["A spiral of selected colours."](Graphics/spiral_test.pdf "A spiral of selected colours.")

## License

Except where otherwise noted, the example programs and other software provided here are made available under the [OSI](http://opensource.org/)-approved [MIT License](http://opensource.org/licenses/mit-license.html).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
