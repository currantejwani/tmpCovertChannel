# Covert Channel Based on File Size

## Introduction
This project provides a proof-of-concept for a covert communication channel using the size of a file as a signal. Specifically, the sender modifies the size of a file to send binary data, and the receiver interprets the size of the file to decode the data. Synchronization between the sender and receiver is achieved using additional files as signals.

## How It Works
- **The sender encodes each bit of a message by changing the size of a file.**
  - `0` bit results in an even file size.
  - `1` bit results in an odd file size.
- **After sending each bit**, the sender creates a "Data Send Ready" (DSR) file to notify the receiver that a new bit has been sent.
- **The receiver**, upon detecting the DSR file, reads the bit from the size of the file and then deletes the DSR file to acknowledge the reading.
- **Completion Signal**: Once the sender has transmitted the entire message, it signals completion by creating a "Data Send Complete" (DSC) file. The receiver stops listening upon detecting this file.

## How to Run
1. Ensure Python is installed on your machine.
2. Clone this repository or download the sender and receiver Python scripts.
3. Open two terminal windows (or command prompts). In one, you'll run the receiver, and in the other, you'll run the sender.
4. First, start the receiver by executing: `python3 receiver.py`
5. Next, start the sender by executing: `python3 sender.py`
6. When prompted on the sender terminal, input your message.
7. Watch as the receiver decodes the message.

## Example
<img width="461" alt="sent" src="https://github.com/currantejwani/tmpCovertChannel/assets/41889986/634749b8-5c53-4d7b-a556-dd22add0cda1">
<img width="461" alt="received" src="https://github.com/currantejwani/tmpCovertChannel/assets/41889986/8ce5d2d6-ea0b-461a-8150-41ada5cce637">

