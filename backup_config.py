#!./venv/bin/python
"""This script takes a backup of all the devices on the topology."""
from nornir.plugins.tasks import networking #pylint: disable=import-error
from nornir.plugins.functions.text import print_result #pylint: disable=import-error
from nornir.plugins.tasks.files import write_file #pylint: disable=import-error
from nornir import InitNornir #pylint: disable=import-error

BACKUP_PATH = "./data/configs"


def backup_config(task): # pylint: disable=missing-function-docstring
    task.run(task=networking.napalm_get, getters=["interfaces_ip"])
    # task.run(
    #     task=write_file,
    #     content=r_var.result["config"]["running"],
    #     filename=f"{path}/{task.host}.txt",
    # )


NR = InitNornir(config_file="./config.yaml")

RESULT = NR.run(
    name="Backup Device configurations",
     #path=BACKUP_PATH, 
     task=backup_config
)

print_result(RESULT)
