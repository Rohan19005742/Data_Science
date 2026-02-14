#!/usr/bin/env python3
"""
Drawing Board Application
A simple interactive drawing application using tkinter and PIL.
"""

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw
import os


class DrawingBoard:
    """Main Drawing Board application class."""
    
    def __init__(self, root):
        """Initialize the drawing board application."""
        self.root = root
        self.root.title("Drawing Board")
        
        # Canvas settings
        self.canvas_width = 800
        self.canvas_height = 600
        self.bg_color = "white"
        
        # Drawing settings
        self.pen_color = "black"
        self.pen_width = 2
        self.eraser_mode = False
        self.last_x = None
        self.last_y = None
        
        # Setup UI
        self.setup_ui()
        
        # Setup PIL Image for saving
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)
        
    def setup_ui(self):
        """Setup the user interface."""
        # Create toolbar frame
        toolbar = tk.Frame(self.root, bg="lightgray")
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Color selection button
        color_btn = tk.Button(toolbar, text="Choose Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Preset color buttons
        colors = ["black", "red", "green", "blue", "yellow", "orange", "purple", "pink"]
        for color in colors:
            btn = tk.Button(toolbar, bg=color, width=3, 
                          command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=2, pady=5)
        
        # Pen width control
        tk.Label(toolbar, text="Width:", bg="lightgray").pack(side=tk.LEFT, padx=5)
        self.width_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL,
                                    command=self.change_width)
        self.width_scale.set(self.pen_width)
        self.width_scale.pack(side=tk.LEFT, padx=5)
        
        # Eraser button
        self.eraser_btn = tk.Button(toolbar, text="Eraser", command=self.toggle_eraser)
        self.eraser_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Clear button
        clear_btn = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Save button
        save_btn = tk.Button(toolbar, text="Save", command=self.save_drawing)
        save_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, 
                               height=self.canvas_height, bg=self.bg_color)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
    def choose_color(self):
        """Open color chooser dialog."""
        color = colorchooser.askcolor(title="Choose color")
        if color[1]:
            self.set_color(color[1])
            
    def set_color(self, color):
        """Set the pen color."""
        self.pen_color = color
        self.eraser_mode = False
        self.eraser_btn.config(relief=tk.RAISED)
        
    def change_width(self, width):
        """Change the pen width."""
        self.pen_width = int(width)
        
    def toggle_eraser(self):
        """Toggle eraser mode."""
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_btn.config(relief=tk.SUNKEN)
        else:
            self.eraser_btn.config(relief=tk.RAISED)
            
    def start_draw(self, event):
        """Start drawing."""
        self.last_x = event.x
        self.last_y = event.y
        
    def draw_line(self, event):
        """Draw a line on the canvas."""
        if self.last_x and self.last_y:
            current_color = self.bg_color if self.eraser_mode else self.pen_color
            
            # Draw on tkinter canvas
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=self.pen_width, fill=current_color,
                capstyle=tk.ROUND, smooth=tk.TRUE
            )
            
            # Draw on PIL image for saving
            self.draw.line(
                [self.last_x, self.last_y, event.x, event.y],
                fill=current_color, width=self.pen_width
            )
            
        self.last_x = event.x
        self.last_y = event.y
        
    def stop_draw(self, event):
        """Stop drawing."""
        self.last_x = None
        self.last_y = None
        
    def clear_canvas(self):
        """Clear the canvas."""
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)
        
    def save_drawing(self):
        """Save the drawing to a file."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.image.save(file_path)
                messagebox.showinfo("Success", f"Drawing saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save drawing: {str(e)}")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = DrawingBoard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
