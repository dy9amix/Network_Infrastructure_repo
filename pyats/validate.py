from genie.harness.main import gRun
from genie.conf.base import Device
from pyats.easypy import run
import os
from genie import testbed
from pyats import topology

test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    # pts_features mentions to Genie which feature to learn in CommonSetup, and then compare at the CommonCleanup
    # trigger_uids and verification_uids limit which test to execute
    # test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testbedfile = ('/home/segunorodeji_gmail_com/Projects/Network_Infrastructure_repo/pyats/testbed/testbed_R2.yaml')
    testbed_1 = topology.loader.load(testbedfile)
    testscript_1 = gRun(verification_datafile='/usr/local/lib/python3.8/dist-packages/genie/libs/sdk/genie_yamls/verification_datafile.yaml',
         devices=['R2'], verification_uids=['Verify_IpInterfaceBrief'], testbed=testbed_1)
