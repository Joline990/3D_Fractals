import mido

input_port = mido.open_input('LPD8 mk2')
message = input_port.receive()

for message in input_port:
    print(message)