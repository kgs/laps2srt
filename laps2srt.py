#!/usr/bin/python

import sys
from datetime import timedelta

def format_srt_time(td):
  hours, remainder = divmod(td.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return '{:02d}:{:02d}:{:02d},{:03d}'.format(hours, minutes, seconds, td.microseconds/1000)

def format_lap_time(td):
  return '{:02d}:{:03d}'.format(td.seconds, td.microseconds/1000)

def write_record(nr, start, end, lap_time):
  print nr
  print '{} --> {}'.format(format_srt_time(start), format_srt_time(end))
  print format_lap_time(lap_time)
  print ''

def main():
  if len(sys.argv) != 2:
    print 'usage: {} lap_times.txt'.format(sys.argv[0])
    print ''
    print 'lap_times.txt has start offset in first line, empty line'
    print 'and then lap times in following lines'
    sys.exit(1)

  with open(sys.argv[1]) as f:
    lines = f.readlines()

  offset = timedelta(seconds=float(lines[0].strip()))

  laps = []
  for i in range(2, len(lines)):
    laps.append(timedelta(seconds=float(lines[i].strip())))

  end = offset
  for x in range(0, len(laps)):
    start = end
    end = start + laps[x]
    write_record(x+1, start, end, laps[x])

if __name__ == '__main__':
  main()
