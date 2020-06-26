from nornir import InitNornir
from nornir_config.interfaces_config import load_data
from nornir.plugins.functions.text import print_result

def main():
    nr = InitNornir("./config.yaml")
    r = nr.run(task=load_data)
    print_result(r)

if __name__ == "__main__":
    main()