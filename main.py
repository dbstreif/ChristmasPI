from apa102 import APA102
from time import sleep

def christmas_special(module: APA102) -> None:
    module.clear_strip()
    i = 0
    while True:
        if i == 0:
            for led in range(60):
                if led == 0:
                    module.set_pixel(led, 255, 0, 0)
                    module.show()
                
                else:
                    module.set_pixel(led, 255, 0, 0)
                    module.show()
                    sleep(.01)
                    module.clear_pixel(led)
                    module.set_pixel(led - 1, 0, 255, 0)
                    module.show()
                    
                sleep(.01)
                module.clear_strip()
            i = 1
            
        elif i == 1:
            led_count = module.led_count - 1
            for led in range(60):
                if led == 0:
                    module.set_pixel(led_count - led, 255, 0, 0)
                    module.show()
                
                else:
                    module.set_pixel(led_count - led, 255, 0, 0)
                    module.show()
                    sleep(.01)
                    module.clear_pixel(led_count - led)
                    module.set_pixel(led_count - led + 1, 0, 255, 0)
                    module.show()
                    
                sleep(.01)
                module.clear_strip()
            i = 0














if __name__ == "__main__":
    module = APA102(led_count=60)
    christmas_special(module)
