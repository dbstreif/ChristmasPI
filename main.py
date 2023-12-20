from spidev import SpiDev

spi = SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 4000
msg = [0b00000000000000000000000000000000, 0b11100000000000000000000000000, 0b11111111111111111111111111111111]

while True:
    spi.xfer(msg)

spi.close()