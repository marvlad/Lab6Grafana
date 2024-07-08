import re

# Define a function to extract numeric values from a string
def extract_numeric(text):
    return float(re.search(r'[-+]?\d*\.\d+|\d+', text).group())

# Define the file path
file_path = 'raw_log.txt'
file_path = 'logs/LastLog.txt'

# Define variables to store extracted values
humidity = None
temperature = None
thermistor = None
LV_3_3 = None
LV_3_1 = None
LV_1_8 = None
Photodiode = None
Saltbridge = None
dac0 = None
dac1 = None

# Open the file and read line by line
with open(file_path, 'r') as file:   
    for line in file:             
        if line.startswith('humidity'):
            humidity = extract_numeric(line)
        elif line.startswith('temperature'):
            temperature = extract_numeric(line)
        elif line.startswith('thermistor'):    
            thermistor = extract_numeric(line)
        elif line.startswith('LV voltages'):  
            voltages = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            LV_3_3 = float(voltages[1])  # Index 1 corresponds to V(3.3)
            LV_3_1 = float(voltages[3])  # Index 3 corresponds to V(3.1)
            LV_1_8 = float(voltages[5])  # Index 5 corresponds to V(1.8)
        elif line.startswith('Photodiode'):                             
            Photodiode = extract_numeric(line)
        elif line.startswith('Saltbridge return'):
            Saltbridge = extract_numeric(line)    
        elif line.startswith('Threshold for DAC 0 is'):
            dac0 = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        elif line.startswith('Threshold for DAC 1 is'):
            dac1 = re.findall(r'[-+]?\d*\.\d+|\d+', line)
                                              
# Print the extracted values in the desired format
print("# HELP humidity The humidity level")
print("# TYPE humidity gauge")
print('humidity{location="indoors"}', humidity)
print("# HELP temperature The temperature in Celsius")
print("# TYPE temperature gauge")
print('temperature{location="indoors"}', temperature)
print("# HELP thermistor Thermistor reading")
print("# TYPE thermistor gauge")
print('thermistor{location="indoors"}', thermistor)
print("# HELP lv1 Voltage level 1")
print("# TYPE lv1 gauge")
print('lv1{location="indoors"}', LV_3_3)
print("# HELP lv2 Voltage level 2")
print("# TYPE lv2 gauge")
print('lv2{location="indoors"}', LV_3_1)
print("# HELP lv3 Voltage level 3")
print("# TYPE lv3 gauge")
print('lv3{location="indoors"}', LV_1_8)
print("# HELP photodiode Photodiode reading")
print("# TYPE photodiode gauge")
print('photodiode{location="indoors"}', Photodiode)
print("# HELP saltbridge Saltbridge reading")
print("# TYPE saltbridge gauge")
print('saltbridge{location="indoors"}', Saltbridge)
print("# HELP dac0 dac0 reading")
print("# TYPE dac0 gauge")
print('dac0{location="indoors"}', dac0[1])
print("# HELP dac1 dac1 reading")
print("# TYPE dac1 gauge")
print('dac1{location="indoors"}', dac1[1])
