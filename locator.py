import tkinter as tk


class TransparentWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.attributes("-alpha", 0.3)
        self.attributes("-topmost", True)
        self.title("Transparent Window")
        self.overrideredirect(True)
        self.bind("<Button-1>", self.on_click)
        self.points = []

        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.configure(bg=self.cget("bg"))

    def on_click(self, event):
        x, y = event.x_root, event.y_root
        self.points.append((x, y))

        # add red points after clicking
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", outline="red")

        if len(self.points) == 4:
            self.print_points()
            self.points = []
            self.quit()

    def print_points(self):
        point_dict = {}
        for i, point in enumerate(self.points, start=1):
            point_dict[f"x{i}"] = point[0]
            point_dict[f"y{i}"] = point[1]

        print(point_dict)


if __name__ == "__main__":
    app = TransparentWindow()
    app.mainloop()
