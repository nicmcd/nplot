#!/usr/bin/env python3

import nplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

lp = nplot.LinePlot(plt, x, [y1, y2, y3])
lp.set_title('Trigonometric Functions')
lp.set_data_labels(['sin(x)', 'cos(x)', 'tan(x)'])
lp.set_xlabel('x')
lp.set_ylabel('y')
lp.set_ylimits(-5, 5)
lp.plot('line.png')
