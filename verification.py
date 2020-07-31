from nornir import InitNornir
from pyats.validations.validate_interfaces import main as verifyInterfaces
from pyats.validations.validate_ospf import main as verifyOspf
from pyats.validations.validate_route import main as verifyRoute
from nornir.core.filter import F


nr = InitNornir("/home/segunorodeji_gmail_com/Projects/Network_Infrastructure_repo/config.yaml")
# All run() must be inside a main function
def main():
    nr.run(task=verifyInterfaces) #verify Interface configurations on all devices 
    nr.run(task=verifyRoute) #verify IP routes for all devices

    ospf_device = nr.filter(F(name="R1")|F(name="R2")|F(name="R3")|F(name="R10")|F(name="R11")|F(name="R12"))
    ospf_device.run(task=verifyOspf)