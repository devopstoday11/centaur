# feature 1 - mean acceleration

import sys

WINDOW_LENGTH = 5.0

window_data = []
window_total = 0.0

def push_data(time, accel):
  global window_data, window_total
  window_data.append({ 'time': time, 'accel': accel })
  window_total += accel

def pop_data():
  global window_data, window_total
  head = window_data.pop(0)
  window_total -= head['accel']

def expire_data(window_end):
  global window_data, window_total
  window_begin = window_end - WINDOW_LENGTH
  while 1:
    head = window_data[0]
    if (head['time'] > window_begin):
      break
    pop_data()

for line in sys.stdin:
  split = line.split(' ')
  time = float(split[0])
  accel = float(split[1])

  # push new data to the window
  push_data(time, accel)

  # expire old data from the window
  expire_data(time)

  mean_accel = window_total / len(window_data)
  print("%f %f" % (time, mean_accel))
