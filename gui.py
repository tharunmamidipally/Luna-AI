import tkinter as tk
import threading
import time

class LunaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Luna Voice Assistant")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()
        self.circles = []
        self.running = False

    def start_ripple(self):
        self.running = True
        threading.Thread(target=self.animate).start()

    def stop_ripple(self):
        self.running = False
        self.canvas.delete("all")

    def animate(self):
        while self.running:
            x, y = 200, 200
            circle = self.canvas.create_oval(x-10, y-10, x+10, y+10, outline="cyan")
            self.circles.append(circle)
            self.fade()
            time.sleep(0.1)

    def fade(self):
        for c in self.circles:
            self.canvas.itemconfig(c, outline="black")
        self.circles.clear()

    def run(self):
        self.root.mainloop()
