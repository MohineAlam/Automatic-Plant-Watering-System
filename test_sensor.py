# import your libraries
import explorerhat
# read humidity from sensor - this should be attached to analogue (analog) one
print("Running sensor test...")
def read_sensor():
 explorerhat.output.one.on()
 time.sleep(1)
 read = explorerhat.analog.one.read()
 explorerhat.output.one.off()
 return read

# return read
sensor_value = read_sensor()
print(f"The voltage from you sensor is: {sensor_value}")
