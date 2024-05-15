import time
import os
import webbrowser
import screen_brightness_control as sbc
import ctypes
import winreg
from pynput.keyboard import Key, Controller as KeyboardController

def set_volume_to_100():
    try:
        # Set volume to maximum
        ctypes.windll.winmm.waveOutSetVolume(0, 0xFFFF)
        print("Volume set to 100%")
    except Exception as e:
        print(f"Failed to set volume: {e}")

def set_brightness_to_100():
    try:
        sbc.set_brightness(100)
        print("Brightness set to 100%")
    except Exception as e:
        print(f"Failed to set brightness: {e}")

def set_desktop_background(image_path):
    try:
        # Use ctypes to call the SystemParametersInfo function
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        print("Desktop background set to", image_path)
    except Exception as e:
        print(f"Failed to set desktop background: {e}")

def set_desktop_icon(icon_path):
    try:
        # Set desktop icon to captainKarat.png
        icon_path = os.path.abspath(icon_path)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\DefaultIcon", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, icon_path)
        print("Desktop icon set to", icon_path)
    except Exception as e:
        print(f"Failed to set desktop icon: {e}")

def open_web_link(url):
    try:
        # Append time parameter to the YouTube URL to skip to 2 minutes and 31 seconds
        url_with_time = url + "&t=2m31s"
        webbrowser.open(url_with_time)
        print("Web link opened:", url_with_time)
    except Exception as e:
        print(f"Failed to open web link: {e}")

if __name__ == "__main__":
    # Directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define image files in the order you want to set them as background
    image_files = ["num3.jpg", "num2.jpg", "num1.jpg", "captainKarat.png"]

    set_volume_to_100()
    set_brightness_to_100()

    for image_file in image_files:
        image_path = os.path.join(script_dir, image_file)
        set_desktop_background(image_path)
        time.sleep(1)  # Wait for 1 second before setting the next image

    # Set desktop icon to captainKarat.png
    icon_file = os.path.join(script_dir, "captainKarat.png")
    set_desktop_icon(icon_file)

    # URL to open
    link_to_open = "https://www.youtube.com/watch?v=Y9eBvwL21Yk"  # Replace with your desired URL
    open_web_link(link_to_open)
