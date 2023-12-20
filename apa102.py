from spidev import SpiDev

class APA102():
    def __init__(self, led_count: int, spi_max_speed_hz=1000000, chipselect=0) -> None:
        self.max_speed_hz = spi_max_speed_hz
        self._spi = None
        self.chipselect = chipselect
        self.led_count = led_count
        self.buf_size = 4
        self.sof_length = 4
        self.eof_length = 4
        self.buffer = self.buffer_init()
            
        #initialize SPIDEV
        
        self._spi = SpiDev(0, self.chipselect)
        self._spi.max_speed_hz = self.max_speed_hz
        
        
    def buffer_init(self):
        buffer = []
        for i in range(self.sof_length):
            buffer.append(0b00000000)
            
        for _ in range(self.led_count):
            buffer += [0b11111111]
            buffer += [0b00000000 for i in range(self.buf_size - 1)]
        
        for i in range(self.eof_length):
            buffer.append(0b11111111)
                    
        return buffer
        
        
    def show(self):
        if self._spi is not None:
            self._spi.xfer3(self.buffer)
            
    def set_pixel(self, x: int, r: int, g: int, b:int):
        """Set a single pixel

        :param x: x index of pixel
        :param r: amount of red (0 to 255)
        :param g: amount of green (0 to 255)
        :param b: amount of blue (0 to 255)

        """
        if x >= self.led_count:
            raise ValueError(f"LED index must be less than {self.led_count}!")
        
        else:
            offset = self.sof_length + (x * 4) + 1
            self.buffer[offset:offset + 3] = [b, g, r]
        
    def set_brightness(self, x: int, brightness: float):
        """Set global brightness of a single pixel

        :param x: x index of pixel
        :param brightness: LED brightness (0.0 to 1.0)

        """
        
        if x >= self.led_count:
            raise ValueError(f"LED index must be less than {self.led_count}!")
        
        else:
            offset = self.sof_length + (x * 4)
            self.buffer[offset] = 0b11100000 | int(31 * brightness)
            
        
    def set_global_brightness(self, brightness: float):
        for i in range(self.led_count):
            self.set_brightness(i, brightness)
        
        
    def clear_strip(self):
        for i in range(self.led_count):
            self.set_pixel(i, 0, 0, 0)
        self.show()
        
    def clear_pixel(self, pixel: int):
        self.set_pixel(pixel, 0, 0, 0)
        self.show()
        
        
if __name__ == "__main__":
    apa102 = APA102(led_count=60)
    apa102.set_pixel(0, 0, 0, 255)
    apa102.clear_strip()