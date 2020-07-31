from genie.harness.main import gRun
from genie.conf.base import Device
from pyats.easypy import run
import os
from genie import testbed

# tesbed = testbed(testbed.yaml)

def main(task):
    # pts_features mentions to Genie which feature to learn in CommonSetup, and then compare at the CommonCleanup
    # trigger_uids and verification_uids limit which test to execute
    # test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gRun(verification_datafile='/usr/local/lib/python3.8/dist-packages/genie/libs/sdk/genie_yamls/verification_datafile.yaml',
         devices=[f'{task.host}'], verification_uids=['Verify_IpInterfaceBrief'])