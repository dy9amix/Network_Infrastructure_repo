from genie import testbed
import pprint
testbed = testbed.load('testbed.yaml')
device = testbed.devices['R1']
device.connect()
output = device.learn('ospf')
pprint.pprint(output.info) 
