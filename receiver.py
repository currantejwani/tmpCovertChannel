import os
import time

def bits_to_string(bit_str):
    """
    Convert binary representation back to a string.
    """
    chars = []
    for i in range(0, len(bit_str), 8):
        byte = bit_str[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def detect_signal(filepath):
    """
    Detect signal based on file's size.
    """
    file_size = os.path.getsize(filepath)
    if file_size % 2 == 0:
        return '0'
    else:
        return '1'

filepath = "/tmp/covert_file.txt"
accumulated_bits = ""
received_message = ""

while True:
    if os.path.exists("/tmp/DSC"):  # Check if DSC file exists
        print(f"Complete message received: {received_message}")
        os.remove("/tmp/DSC")
        break
    elif os.path.exists("/tmp/DSR"):  # Check if DSR file exists
        detected_bit = detect_signal(filepath)
        accumulated_bits += detected_bit
        if len(accumulated_bits) == 8:  # When we accumulate 8 bits (1 byte)
            received_char = bits_to_string(accumulated_bits)
            received_message += received_char
            accumulated_bits = ""  # Reset for the next byte
        os.remove("/tmp/DSR")  # Delete the DSR file to acknowledge reading
