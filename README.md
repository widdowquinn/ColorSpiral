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