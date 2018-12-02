from ad_mcp import AdMcp3008
import time

mcp = AdMcp3008()
sensorData = [0, 0, 0, 0, 0, 0, 0, 0]

def getData():
    return sensorData

while True:
    
    sensorData = [mcp.read_adc(0), mcp.read_adc(1), mcp.read_adc(2), mcp.read_adc(3), mcp.read_adc(4), mcp.read_adc(5), mcp.read_adc(6), mcp.read_adc(7)]
    print(str(getData()))
    time.sleep(1)
    
