from genie.harness.main import gRun
from genie.conf.base import Device
from genie import testbed
from pyats import topology


def main(task):
    testbedfile = (f'/home/segunorodeji_gmail_com/Projects/Network_Infrastructure_repo/pyats/testbed/testbed_{task.host}.yaml')
    testbed_1 = topology.loader.load(testbedfile)
    gRun(verification_datafile='/usr/local/lib/python3.8/dist-packages/genie/libs/sdk/genie_yamls/verification_datafile.yaml',
        devices=[f'{task.host}'], verification_uids=['Verify_IpInterfaceBrief'], testbed=testbed_1)