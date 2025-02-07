import rtmidi
import time

midi_in = rtmidi.MidiIn()

ports_dictionary = {k: v for (v, k) in enumerate(midi_in.get_ports())}
midi_in.open_port(ports_dictionary["LPD8 mk2"]) 

while True:
    message_and_dt = midi_in.get_message()
    if message_and_dt:
        (message, dt) = message_and_dt # unpack
        command = hex(message[0])
        channel = message[1]
        print(f"channel = {channel}, command = {command}")

        if channel == 40:
            if command == "0x99":
                print("btn pressed")
            elif command == "0x89":
                print("btn released")
    else:
        time.sleep(0.001)
