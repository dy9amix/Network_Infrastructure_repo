from nornir import InitNornir
from nornir_config.interfaces_config import load_data
from nornir_config.ospf_config import configure_ospf
from nornir_config.rip_config import configure_rip
from nornir_config.eigrp_config import configure_eigrp
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F

nr = InitNornir("./config.yaml")

def interfaces():
    r = nr.run(task=load_data)
    print_result(r)

def route():
    ospf_device = nr.filter(F(name="R1")|F(name="R2")|F(name="R3")|F(name="R10")|F(name="R11")|F(name="R12"))
    r_ospf = ospf_device.run(task=configure_ospf)
    print_result(r_ospf)
    rip_device = nr.filter(F(name="R4")|F(name="R5"))  
    r_rip = rip_device.run(task=configure_rip)
    print_result(r_rip)
    eigrp_device = nr.filter(F(name="R6")|F(name="R7")|F(name="R8")|F(name="R8"))  
    r_eigrp = eigrp_device.run(task=configure_eigrp)
    print_result(r_eigrp)

if __name__ == "__main__":
    route()