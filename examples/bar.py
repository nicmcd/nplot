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

bp = nplot.BarPlot(plt, x, ys)
bp.set_title('Financial Results')
bp.set_data_labels(['Q1', 'Q2', 'Q3', 'Q4'])
bp.set_xlabel('2022')
bp.set_ylabel('Revenue ($)')
bp.set_ymin(0)
bp.set_ymax(max(map(max, ys)) * 1.05)
bp.plot('bar.png')
