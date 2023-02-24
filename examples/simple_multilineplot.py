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

mlp = nplot.MultilinePlot(plt, x, [y1, y2, y3])
mlp.set_title('Trigonometric Functions')
mlp.set_data_labels(['sin(x)', 'cos(x)', 'tan(x)'])
mlp.set_xlabel('x')
mlp.set_ylabel('y')
mlp.set_ylimts(-5, 5)
mlp.plot('simple_multilineplot.png')
