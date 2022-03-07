import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

def write_img_to_csv(filename):
    with open(filename,"w") as outputfile:
        print(amg.pixels)
        for row in amg.pixels:
            outputfile.write(row)
            outputfile.write("\n")

# while True:
#     write_img_to_csv("plot.csv")
#     time.sleep(1)

write_img_to_csv("plot.csv")
