#!/usr/bin/env python3

import nplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = ['Kent', 'Lincoln', 'Mersey']
ys = [[44700, 52800, 43500],
      [45000, 36500, 41000],
      [51200, 44200, 39700],
      [56500, 45300, 41200]]

mbp = nplot.MultibarPlot(plt, x, ys)
mbp.set_title('Financial Results')
mbp.set_data_labels(['Q1', 'Q2', 'Q3', 'Q4'])
mbp.set_xlabel('2022')
mbp.set_ylabel('Revenue ($)')
mbp.set_ymin(0)
mbp.set_ymax(max(map(max, ys)) * 1.05)
mbp.plot('simple_multibarplot.png')
