import subprocess









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

choose_and_open()


