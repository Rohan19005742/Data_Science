#!/usr/bin/env python3
"""
Simple example demonstrating the Drawing Board application.
This script creates a simple drawing programmatically.
"""

from PIL import Image, ImageDraw

def create_example_drawing():
    """Create a simple example drawing."""
    # Create a new image
    width, height = 400, 300
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Draw a smiley face
    # Face circle
    draw.ellipse([100, 50, 300, 250], outline="black", width=3)
    
    # Eyes
    draw.ellipse([140, 100, 170, 130], fill="black")
    draw.ellipse([230, 100, 260, 130], fill="black")
    
    # Smile
    draw.arc([130, 120, 270, 220], start=0, end=180, fill="black", width=3)
    
    # Save the image
    output_path = "example_drawing.png"
    image.save(output_path)
    print(f"Example drawing saved to {output_path}")
    
    return image

if __name__ == "__main__":
    create_example_drawing()
