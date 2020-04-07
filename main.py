from bm import HumanBenchmark

bm = HumanBenchmark()

red = hex(0x3626ce)
green = hex(0x6adb4b)

while True: 
    x, y = bm.mouse_pos()
    if bm.wait_for_pixel(x, y, red, 0.1):
        bm.wait_and_click(x, y, green, timeout=10)
