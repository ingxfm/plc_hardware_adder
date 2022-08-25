from catalog import Module
from os import system, name
from time import sleep

# TODO 1 Print report
# TODO 2 Check resources are sufficient
# TODO 3 Process power
# TODO 4 Check transactions are successful
# TODO 5 Install modules


clear_console = lambda: system('cls' if name in ('nt', 'dos') else 'clear')

plc_hardware = []
machine_on = 1
# step 1
while machine_on:
    print("Choose 1 for CPU\n"
          "Choose 2 for Analog Inputs module (AI)\n"
          "Choose 3 for Analog Outputs module (AQ))\n"
          "Choose 4 for Analog Inputs Outpus module (AX)\n"
          "Choose 5 for Digital Inputs (DI)\n"
          "Choose 6 for Digital Outputs (DQ)\n"
          "Choose 7 for Digital Inputs Outputs (DX)\n")
    choose = input("Please choose a module:")
    catalog = Module(choose)
    plc_hardware.append(catalog)

    working = input("do you want to continue adding modules? Type 'y' for yes, otherwise it will stop.").lower()
    if working == 'y':
        machine_on = 1
    else:
        machine_on = 0
        clear_console()
    clear_console()


print(f"You have a PLC with {len(plc_hardware)} modules, including the CPU module."
      f"The modules are:\n")
for item in plc_hardware:
    print(f"- The {item.name} with {item.input_quantity} inputs and {item.output_quantity} outputs.")