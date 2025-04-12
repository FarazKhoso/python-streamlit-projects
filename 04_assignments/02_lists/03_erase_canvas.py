# Implement an 'eraser' on a canvas
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Canvas setup
CELL_SIZE = 10
ROWS = 20
COLS = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.pack()

        self.cells = []  # store cell rectangles
        self.draw_grid()

        # Eraser init
        self.eraser = self.canvas.create_rectangle(0, 0, CELL_SIZE*2, CELL_SIZE*2, fill="white", outline="black")

        # Bind mouse motion to move eraser
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def draw_grid(self):
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                row_cells.append(rect)
            self.cells.append(row_cells)

    def move_eraser(self, event):
        # Move eraser rectangle to mouse position
        x1 = event.x - CELL_SIZE
        y1 = event.y - CELL_SIZE
        x2 = event.x + CELL_SIZE
        y2 = event.y + CELL_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check collision with cells
        for row in self.cells:
            for rect in row:
                coords = self.canvas.coords(rect)
                if self.rect_overlap((x1, y1, x2, y2), coords):
                    self.canvas.itemconfig(rect, fill="white")

    def rect_overlap(self, r1, r2):
        # Check if two rectangles overlap
        return not (r1[2] < r2[0] or r1[0] > r2[2] or r1[3] < r2[1] or r1[1] > r2[3])

# Run the app
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
