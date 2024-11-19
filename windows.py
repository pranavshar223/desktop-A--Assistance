import subprocess

# brightness control lib
import wmi

# volume control lib
from pycaw.pycaw import AudioUtilities
from pycaw.constants import AudioDeviceRole
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


def open_application(app_name):
    """
    Open an application by its name or full path using the 'start' command.
    
    Parameters:
    app_name (str): The name of the application or its executable file.
    """
    try:
        subprocess.run(["start", app_name], shell=True, check=True)
        print(f"Successfully launched {app_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open {app_name}. Error: {e}")


def choose_and_open():
    apps = {
        "1": "spotify",
        "2": "telegram",
        "3": "whatsapp",
        "4": "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2023.2.2\\bin\\idea64.exe"
    }

    print("Available Applications:")
    for key, app in apps.items():
        print(f"{key}: {app}")

    choice = input("Enter the number of the application you want to open: ")
    if choice in apps:
        open_application(apps[choice])
    else:
        print("Invalid choice. Please try again.")

choose_and_open("spotify")


def Settings(page=""):
# Open Windows Settings or a specific settings page
    command = ["start", "ms-settings:" + page] if page else ["start", "ms-settings:"]
    subprocess.run(command, shell=True, check=True)

def set_brightness(brightness: int):
    # Create a WMI object to interact with Windows management
    w = wmi.WMI(namespace="wmi")
    
    # Get the current monitor brightness setting
    methods = w.WmiMonitorBrightnessMethods()

    # Set the brightness
    for method in methods:
        method.WmiSetBrightness(Brightness=brightness, Timeout=1)

def set_volume(level: int):
    # PowerShell command to set system volume
    command = f"powershell (Get-WmiObject -Class Win32_SoundDevice).SetVolume({level})"
    subprocess.run(command, shell=True)

def set_volume(level: float):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        AudioUtilities.IID_IAudioEndpointVolume,
        CLSCTX_ALL, None)
    volume = cast(interface, POINTER(AudioUtilities.IAudioEndpointVolume))

    # Set the volume level (float value between 0.0 and 1.0)
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)


# set_volume(50.0)
