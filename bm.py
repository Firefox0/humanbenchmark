import win32gui, mouse, time

class HumanBenchmark:

    def __init__(self):
        self.hwnd = win32gui.GetDesktopWindow()

    def mouse_pos(self):
        return win32gui.GetCursorPos()

    def get_pixel(self, x, y):
        hdc = win32gui.GetWindowDC(self.hwnd)
        color = win32gui.GetPixel(hdc, x, y)
        return hex(color)

    def wait_for_pixel(self, x, y, color, timeout=3):
        start = time.perf_counter()
        while True:
            if self.get_pixel(x, y) == color:
                return 1
            if time.perf_counter()-start >= timeout:
                return 0
            time.sleep(0.1)

    def wait_and_click(self, x, y, color, move=True, timeout=3):
        if self.wait_for_pixel(x, y, color, timeout):
            if move:
                mouse.move(x, y)
            mouse.click()
            return 1
        return 0