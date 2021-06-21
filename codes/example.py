
def logToEcu(ecu):
    print(ecu.replace('cos', '*np.cos').replace('sin', '*np.sin'))

ecu = '-49.74cos(47.12*x) + -11.37'

logToEcu(ecu)