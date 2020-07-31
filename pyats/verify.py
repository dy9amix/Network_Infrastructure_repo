import logging
from pyats import aetest
from genie.harness.standalone import run_genie_sdk, GenieStandalone
from genie.conf import Genie
from genie.conf.base import Device


log = logging.getLogger(__name__)

class common_setup(aetest.CommonSetup):
    @aetest.subsection
    def sample_subsection_1(self):
        """ Common Setup subsection """
        log.info("Aetest Common Setup ")

    @aetest.subsection
    def connect(self, testbed):
        pass
        #genie_testbed = Genie.init(testbed)
        #self.parent.parameters['testbed'] = genie_testbed
        #uut = genie_testbed.devices['uut']
        #uut.connect()


class Verify_Interfaces(GenieStandalone):
    verifications = ['Verify_IpInterface', 'Verify_IpInterfaceBrief']

    @ aetest.test
    def simple_test_1(self, steps):
        """ Sample test section. Only print """
        log.info("This verifies interfaces on all devices")
        # Run genie triggers and verifications
        run_genie_sdk(self, steps,['Verify_IpInterface', 'Verify_IpInterfaceBrief'])

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsections as wanted
    # here is an example of 1 subsection

    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup ")