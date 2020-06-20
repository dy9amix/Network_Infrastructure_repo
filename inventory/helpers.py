from nornir.core.inventory import ConnectionOptions

creds = {
    "R1": {"username": "admin", "password": "admin"},
    "R2": {"username": "admin", "password": "admin"},
    "R3": {"username": "admin", "password": "admin"},
    "R4": {"username": "admin", "password": "admin"},
    "R5": {"username": "admin", "password": "admin"}, 
    "R6": {"username": "admin", "password": "admin"},
    "R7": {"username": "admin", "password": "admin"},
    "R8": {"username": "admin", "password": "admin"},
    "R9": {"username": "admin", "password": "admin"},
    "R10": {"username": "admin", "password": "admin"},
    "R11": {"username": "admin", "password": "admin"},
    "R12": {"username": "admin", "password": "admin"}
    }

def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]
    # host.connection_options["napalm"] = ConnectionOptions(
    #  extras={
    #      "optional_args": {
    #          "secret":"admin"
    #         }
    #     }
    # )