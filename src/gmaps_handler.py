import random
import time
import gc_handler
from playwright.sync_api import sync_playwright

def wait_for_tiles_to_load(page, idle_time=1.0, timeout=10.0):
    """
    Waits until Google Maps tiles have finished loading, including detailed layers.
    idle_time: how long network must be idle (in seconds)
    timeout: max time to wait (in seconds)
    """
    start_time = time.time()
    active_requests = set()

    def handle_request(request):
        if '/maps/vt' in request.url:
            active_requests.add(request.url)

    def handle_finished(request):
        if request.url in active_requests:
            active_requests.remove(request.url)

    page.on('request', handle_request)
    page.on('requestfinished', handle_finished)
    page.on('requestfailed', handle_finished)

    # Wait for a period of no new tile activity
    last_active = time.time()
    while True:
        if not active_requests:
            if time.time() - last_active >= idle_time:
                break
        else:
            last_active = time.time()

        if time.time() - start_time > timeout:
            print("Warning: tile load wait timed out.")
            break
        time.sleep(0.1)

def save_gmaps_image():
    print("Loading gmaps image...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            viewport={"width": 1280, "height": 1000}
        )

        page = context.new_page()
        page.goto("https://www.google.com/maps/place/Majestic+Elegance+Costa+Mujeres/@21.2783167,-86.8204565,1083m/data=!3m1!1e3!4m9!3m8!1s0x8f4c318a57aa36e7:0xc3ed13366f9e5d55!5m2!4m1!1i2!8m2!3d21.2811059!4d-86.8200595!16s%2Fg%2F11h07gcl3z?entry=ttu&g_ep=EgoyMDI1MDYyMy4yIKXMDSoASAFQAw%3D%3D")
        
        print("Moving and zooming...")
        # Move or zoom to force full tile load
        numMoves = random.randint(1, 3)
        for i in range(numMoves):
            page.keyboard.press("ArrowUp")     # Pan north
            page.wait_for_timeout(500)
            page.keyboard.press("ArrowDown")   # Pan back
            page.wait_for_timeout(500)

        # Or zoom in and out
        for i in range(numMoves):
            page.keyboard.press("+")
            page.wait_for_timeout(500)
            page.keyboard.press("-")


        print("Waiting for tiles to load...")
        wait_for_tiles_to_load(page)
        page.wait_for_timeout(15000)
        
        print("Saving gmaps image...")
        page.screenshot(
            path='src/screenshots/new_gmaps_screenshot.jpeg',
            clip={ 'x': 500, 'y': 200, 'width': 650, 'height': 650 },
            type='jpeg',
            quality=100,
        )

        browser.close()
    print("Gmaps image saved")
if __name__ == "__main__":
    save_gmaps_image()