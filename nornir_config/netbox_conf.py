import re
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.data import load_yaml
from nornir import InitNornir
import pynetbox
from netbox import NetBox

path = "./nornir_config/values"
nb_url = 'http://35.208.97.187'
nb_token = 'ac072a2c5733b55af66b27a4cb8179a7f314a9c7'
ssl_verify = False
nb_port = 8000
url = f"{nb_url}:{nb_port}"
py_netbox = pynetbox.api(url, token=nb_token)
nb_host = re.sub("^.*//|:.*$", "", nb_url)
netbox = NetBox(host=nb_host, port=8000, use_ssl=False, auth_token=nb_token)
nb_interfaces = netbox.dcim.get_interfaces()

def is_interface_present(nb_interfaces, device_name, interface_name):
    for i in nb_interfaces:
        if i["name"] == interface_name and i["device"]["display_name"] == device_name:
            return True
    return False

def update_netbox_interface(task, nb_interfaces):
    data = task.run(
                     task=load_yaml,
              file=f'{path}/{task.host}.yaml'
       )
    task.host["interface"] = data.result["interface"]
    r = task.run(task=networking.napalm_get, getters=["interfaces", "interfaces_ip"])
    interfaces = r.result["interfaces"]
    interfaces_ip = r.result["interfaces_ip"]
    for interface_name in interfaces.keys():
        interface_id = list(interfaces_ip.keys())[0]
        mac_address = interfaces[interface_name]["mac_address"]
        print("mac address: ",mac_address)
        if mac_address == "None" or mac_address == "Unspecified":
            mac_address = "ee:ee:ee:ee:ee:ee"

        description = interfaces[interface_name]["description"]
        ip_list = interfaces_ip[interface_name]["ipv4"]
        ip_address = list(ip_list.keys())[0]
        prefix_len= interfaces_ip[interface_name]["ipv4"][ip_address]['prefix_length']
        ip = f"{ip_address}/{prefix_len}"
        ip_dict = {
            "address":ip,
            "status":"active",
            "interface":{"name":interface_id, "device":{"name":f"{task.host}"}}
        }
        if is_interface_present(nb_interfaces, f"{task.host}", interface_name):
            print(
                f"* Updating Netbox Interface for device {task.host}, interface {interface_name}"
            )
            netbox.dcim.update_interface(
                device=f"{task.host}",
                interface=interface_name,
                description=description,
                #mac_address=mac_address,
            )
            ip_print = py_netbox.ipam.ip_addresses.create(ip_dict)
            print("New IP: ",ip_print)

