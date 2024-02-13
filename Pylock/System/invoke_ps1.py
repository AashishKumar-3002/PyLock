import subprocess

def invoke_lock_script():
    # Path to the PowerShell script
    script_path = "Pylock\System\lock_laptop.ps1"

     # Call the PowerShell script using subprocess with ExecutionPolicy Bypass
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path], shell=True)
