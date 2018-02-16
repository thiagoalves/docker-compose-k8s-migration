#!/usr/bin/env python

import sys

def get_data(line):
  data = line.replace('-', '').replace('"', '').strip().split(':')
  return {
    "name": data[1].lstrip('/').replace('/', '-').replace('.', '-'),
    "hostVol": data[0],
    "containerVol": data[1]
  }

data = sys.stdin.readlines()

print "        volumeMounts:"
for line in data:
  o = get_data(line)
  print "        - mountPath: \"%s\"\n          name: \"{{ container_name }}-%s\"" % (o['containerVol'], o['name'])

print "      volumes:"
for line in data:
  o = get_data(line)
  print "      - name: \"{{ container_name }}-%s\"\n        hostPath:\n          path: \"%s\"\n          type: DirectoryOrCreate" % (o['name'], o['hostVol'])
