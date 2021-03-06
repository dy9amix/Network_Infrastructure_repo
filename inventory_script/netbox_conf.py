import re
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir import InitNornir
from netbox import NetBox
from helpers import is_interface_present

nb_url = 'http://35.208.97.187'
nb_token = 'ac072a2c5733b55af66b27a4cb8179a7f314a9c7'
ssl_verify = False
nb_host = re.sub("^.*//|:.*$", "", nb_url)

netbox = NetBox(host=nb_host, port=32768, use_ssl=False, auth_token=nb_token)

nb_interfaces = netbox.dcim.get_interfaces()


def update_netbox_interface(task, nb_interfaces):
    r = task.run(task=networking.napalm_get, getters=["interfaces"])
    interfaces = r.result["interfaces"]

    for interface_name in interfaces.keys():
        mac_address = interfaces[interface_name]["mac_address"]
        if mac_address == "None" or mac_address == "Unspecified":
            mac_address = "ee:ee:ee:ee:ee:ee"

        description = interfaces[interface_name]["description"]

        if is_interface_present(nb_interfaces, f"{task.host}", interface_name):
            print(
                f"* Updating Netbox Interface for device {task.host}, interface {interface_name}"
            )
            netbox.dcim.update_interface(
                device=f"{task.host}",
                interface=interface_name,
                description=description,
                mac_address=mac_address,
            )
