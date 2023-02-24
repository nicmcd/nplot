#!/usr/bin/env python3

import nplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

x1 = sorted(random.choices(range(1, 100, 1), k=50))
y1 = [random.gauss(mu=1.0, sigma=0.3) for _ in x1]
x2 = sorted(random.choices(range(1, 100, 1), k=50))
y2 = [random.gauss(mu=2.0, sigma=0.4) for _ in x2]
x3 = sorted(random.choices(range(1, 100, 1), k=50))
y3 = [random.gauss(mu=3.0, sigma=0.2) for _ in x3]

msp = nplot.MultiscatterPlot(plt, [x1, x2, x3], [y1, y2, y3])
msp.set_title('50 gaussian random (X,Y) pairs per set)')
msp.set_data_labels(['mu=1.0 sigma=0.3',
                     'mu=2.0 sigma=0.4',
                     'mu=3.0 sigma=0.2'])
msp.set_xlabel('X')
msp.set_xlimits(0, 100)
msp.set_ylabel('Y')
msp.set_yauto_frame(0.05)
msp.set_plot_style('colorful-markers')
msp.plot('simple_multiscatterplot.png')
