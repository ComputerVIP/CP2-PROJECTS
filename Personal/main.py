import pymem

# Attach to Baba Is You
pid = 15532
pm = pymem.Pymem()
pm.open_process_from_id(pid)



'''
import subprocess

def read_memory(address):
    # Run WinDbg in command mode (`cdb.exe`)
    command = f'cdb -p BabaIsYou.exe -c "dd {address} L1; q"'
    
    # Execute command and capture output
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    # Extract memory value from output
    lines = result.stdout.splitlines()
    for line in lines:
        if address in line:
            parts = line.split()
            return int(parts[1], 16)  # Convert hex to integer
    
    return None

# Example: Read Baba's X and Y position
baba_x_addr = "0x12345678"  # Replace with actual memory address
baba_y_addr = "0x12345679"

baba_x = read_memory(baba_x_addr)
baba_y = read_memory(baba_y_addr)

print(f"Baba Position: ({baba_x}, {baba_y})")
import csv
import time

with open("baba_training_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Baba_X", "Baba_Y", "Action"])

    while True:
        baba_x = read_memory(baba_x_addr)
        baba_y = read_memory(baba_y_addr)
        action = input("Enter action (0=Up, 1=Down, 2=Left, 3=Right): ")

        writer.writerow([baba_x, baba_y, action])
        print(f"Logged: {baba_x}, {baba_y}, {action}")

        time.sleep(1)  # Adjust logging frequency

from pynput import keyboard

# Memory addresses (Replace with actual addresses found via WinDbg)
baba_x_addr = "0x12345678"
baba_y_addr = "0x12345679"

# Map key presses to actions
ACTION_MAP = {
    "w": "Up",
    "s": "Down",
    "a": "Left",
    "d": "Right"
}

# Function to read memory via WinDbg
def read_memory(address):
    command = f'cdb -p BabaIsYou.exe -c "dd {address} L1; q"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    # Extract memory value from output
    lines = result.stdout.splitlines()
    for line in lines:
        if address in line:
            parts = line.split()
            return int(parts[1], 16)  # Convert hex to integer
    
    return None

# Open CSV file for logging
with open("baba_training_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Baba_X", "Baba_Y", "Action"])

    def on_press(key):
        try:
            if key.char in ACTION_MAP:
                action = ACTION_MAP[key.char]
                
                # Read Baba's position
                baba_x = read_memory(baba_x_addr)
                baba_y = read_memory(baba_y_addr)

                # Log data
                writer.writerow([baba_x, baba_y, action])
                print(f"Logged: {baba_x}, {baba_y}, {action}")

        except AttributeError:
            pass  # Ignore special keys

    # Start listening for key presses
    with keyboard.Listener(on_press=on_press) as listener:
        print("Listening for key presses... (Press ESC to stop)")
        listener.join()
'''