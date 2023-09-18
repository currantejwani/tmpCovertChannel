import os
import time

def send_signal(filepath, bit):
    """
    Send signal based on file size.
    '0' results in even file size, '1' results in odd file size.
    """
    if bit == '0':
        with open(filepath, 'wb') as f:
            f.write(b'\x00' * 10)  # Write 10 bytes for even size
    else:
        with open(filepath, 'wb') as f:
            f.write(b'\x00' * 11)  # Write 11 bytes for odd size
    open("/tmp/DSR", "w").close()


message = input("Enter your message to be sent in bits: ")
binary_message = ''.join(format(ord(ch), '08b') for ch in message)

filepath = "/tmp/covert_file.txt"

for data_bit in binary_message:
    send_signal(filepath, data_bit)
    while os.path.exists("/tmp/DSR"):  # Wait until receiver acknowledges reading
        time.sleep(1)

# Sending completion signal
open("/tmp/DSC", "w").close()
