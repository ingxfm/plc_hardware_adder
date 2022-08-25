class Module:

    def __init__(self, module_type):
        self.id = 0
        self.name = ""
        self.current_in_mA = 0
        self.input_quantity = 0
        self.output_quantity = 0
        self.current_in_mA = 0
        self.module_catalog = {
            "1": self.cpu_module(),  # cpu
            "2": self.analog_inputs(),  # ai
            "3": self.analog_outputs(),  # aq
            "4": self.analog_inputs_outputs(),  # ax
            "5": self.digital_inputs(),  # di
            "6": self.digital_outputs(),  # dq
            "7": self.digital_inputs_outputs(),  # dx
        }
        self.module_type_selected = self.module_catalog[module_type]

    def cpu_module(self):
        self.id = 1
        self.name = "S7 1500"
        self.current_in_mA = 140
        self.input_quantity = 8
        self.output_quantity = 8

    def analog_inputs(self):
        self.id = 2
        self.name = "SIMATIC ET 200SP, Analog inputs, AI"
        self.current_in_mA = 120
        self.input_quantity = 16
        self.output_quantity = 0

    def analog_outputs(self):
        self.id = 3
        self.name = "SIMATIC ET 200SP, Digital outputs, AQ"
        self.current_in_mA = 120
        self.input_quantity = 0
        self.output_quantity = 16

    def digital_inputs(self):
        self.id = 4
        self.name = "SIMATIC ET 200SP, Digital inputs, DI"
        self.current_in_mA = 120
        self.input_quantity = 16
        self.output_quantity = 0

    def digital_outputs(self):
        self.id = 5
        self.name = "SIMATIC ET 200SP, Digital outputs, DQ"
        self.current_in_mA = 120
        self.input_quantity = 0
        self.output_quantity = 16

    def analog_inputs_outputs(self):
        self.id = 6
        self.name = "SIMATIC ET 200SP, Analog I/O, AX"
        self.current_in_mA = 120
        self.input_quantity = 8
        self.output_quantity = 8

    def digital_inputs_outputs(self):
        self.id = 7
        self.name = "SIMATIC ET 200SP, Digital I/O, DX"
        self.current_in_mA = 120
        self.input_quantity = 8
        self.output_quantity = 8



