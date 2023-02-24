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

sp = nplot.ScatterPlot(plt, [x1, x2, x3], [y1, y2, y3])
sp.set_title('50 gaussian random (X,Y) pairs per set')
sp.set_data_labels(['mu=1.0 sigma=0.3',
                    'mu=2.0 sigma=0.4',
                    'mu=3.0 sigma=0.2'])
sp.set_xlabel('X')
sp.set_xlimits(0, 100)
sp.set_ylabel('Y')
sp.set_yauto_frame(0.05)
sp.set_plot_style('colorful-markers')
sp.plot('scatter.png')
