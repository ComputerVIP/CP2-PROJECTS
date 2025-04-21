import tkinter as tk
from tkinter import ttk
from D2d import Circle, Rectangle, Triangle

repeat = True
'''

    Class Implementation:
        Create separate classes for different shapes: Circle, Rectangle, and Triangle
        Implement a Square class as a subclass of Rectangle Include appropriate attributes for each shape (e.g., radius, length, width, base, height)
    Shape Calculations:
        Implement methods to calculate area and perimeter for each shape
        Create a method to display all information about a shape Include a static method in each class to explain the formulas used
    User Interface:
        Design a text-based menu for interacting with the calculator
        Allow users to create multiple shapes and switch between them
        Include options to perform various calculations on the selected shape
    Validation and Error Handling:
        Implement input validation to ensure positive values for dimensions Handle potential errors (e.g., division by zero, invalid input types)
    Shape Comparisons:
        Create methods to compare two shapes (e.g., has_larger_area(), has_longer_perimeter())
        Implement a feature to sort multiple shapes based on a chosen property (area or perimeter)

Bonus are only available to projects submitted on time that meet ALL of the minimum requirements.
BONUS:

3D Shape Extension 

    Design and implement classes for 3D shapes (3 points)
    Create methods for volume and surface area calculations (4 points)
    Extend the user interface to incorporate 3D shape options (5 points)

Graphical Shape Visualization

    Implement basic shape drawing functionality (3 points)
    Scale drawings appropriately based on shape dimensions (4 points)
    Add labels and measurements to the visual representations (5 points)

Shape Transformation Calculator

(Create functionality to calculate how shapes change when scaled, rotated, or translated. Include methods to determine new coordinates or dimensions after transformations.)

    Implement scaling transformations for all shapes (3 points)
    Add rotation calculations for applicable shapes (4 points)
    Create methods for translation and coordinate shifts (5 points)
'''

def main(repeat):
    while repeat:
        root = tk.Tk()
        root.title('Battle Geometry Calculator')

        # Handle program shutdown when "X" is clicked
        def on_close():
            nonlocal repeat
            repeat = False
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_close)

        rad = tk.StringVar()
        length = tk.StringVar()
        width = tk.StringVar()
        height = tk.StringVar()
        base = tk.StringVar()

        # Configure resizing behavior
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        notebook = ttk.Notebook(root)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)
        frame4 = ttk.Frame(notebook)

        # Circle Calculator
        notebook.add(frame1, text="Crcl")
        circle_area_var = tk.StringVar(value="Area: N/A")
        circle_perimeter_var = tk.StringVar(value="Perimeter: N/A")

        tk.Label(frame1, text='Circle Calculator').grid(column=1, row=0)
        tk.Label(frame1, text='Enter radius:').grid(column=1, row=1)
        tk.Entry(frame1, width=7, textvariable=rad).grid(column=1, row=2, sticky=(tk.W, tk.E))
        tk.Button(frame1, text='Calculate', command=lambda: calculate_circle_properties()).grid(column=1, row=3)

        tk.Label(frame1, textvariable=circle_area_var).grid(column=1, row=4)
        tk.Label(frame1, textvariable=circle_perimeter_var).grid(column=1, row=5)

        def calculate_circle_properties():
            try:
                radius = float(rad.get())
                circle = Circle(radius)
                circle_area_var.set(f"Area: {circle.area():.2f}")
                circle_perimeter_var.set(f"Perimeter: {circle.perimeter():.2f}")
            except ValueError:
                circle_area_var.set("Area: Invalid Input")
                circle_perimeter_var.set("Perimeter: Invalid Input")

        # Rectangle Calculator
        notebook.add(frame2, text="Rect/Sqr")
        rect_area_var = tk.StringVar(value="Area: N/A")
        rect_perimeter_var = tk.StringVar(value="Perimeter: N/A")

        tk.Label(frame2, text='Rectangle Calculator').grid(column=1, row=0)
        tk.Label(frame2, text='Enter Length:').grid(column=1, row=1)
        tk.Entry(frame2, width=7, textvariable=length).grid(column=1, row=2, sticky=(tk.W, tk.E))
        tk.Label(frame2, text='Enter Width:').grid(column=1, row=3)
        tk.Entry(frame2, width=7, textvariable=width).grid(column=1, row=4, sticky=(tk.W, tk.E))
        tk.Button(frame2, text='Calculate', command=lambda: calculate_rect_properties()).grid(column=1, row=5)

        tk.Label(frame2, textvariable=rect_area_var).grid(column=1, row=6)
        tk.Label(frame2, textvariable=rect_perimeter_var).grid(column=1, row=7)

        def calculate_rect_properties():
            try:
                rect_length = float(length.get())
                rect_width = float(width.get())
                rect = Rectangle(rect_length, rect_width)
                rect_area_var.set(f"Area: {rect.area():.2f}")
                rect_perimeter_var.set(f"Perimeter: {rect.perimeter():.2f}")
            except ValueError:
                rect_area_var.set("Area: Invalid Input")
                rect_perimeter_var.set("Perimeter: Invalid Input")

        # Triangle Calculator
        notebook.add(frame3, text="Tri")
        tri_area_var = tk.StringVar(value="Area: N/A")
        tri_perimeter_var = tk.StringVar(value="Perimeter: N/A")

        tk.Label(frame3, text='Triangle Calculator').grid(column=1, row=0)
        tk.Label(frame3, text='Enter Base:').grid(column=1, row=1)
        tk.Entry(frame3, width=7, textvariable=base).grid(column=1, row=2, sticky=(tk.W, tk.E))
        tk.Label(frame3, text='Enter Height:').grid(column=1, row=3)
        tk.Entry(frame3, width=7, textvariable=height).grid(column=1, row=4, sticky=(tk.W, tk.E))
        tk.Button(frame3, text='Calculate', command=lambda: calculate_tri_properties()).grid(column=1, row=5)

        tk.Label(frame3, textvariable=tri_area_var).grid(column=1, row=6)
        tk.Label(frame3, textvariable=tri_perimeter_var).grid(column=1, row=7)

        def calculate_tri_properties():
            try:
                tri_base = float(base.get())
                tri_height = float(height.get())
                tri = Triangle(tri_base, tri_height)
                tri_area_var.set(f"Area: {tri.area():.2f}")
                tri_perimeter_var.set(f"Perimeter: {tri.perimeter():.2f}")
            except ValueError:
                tri_area_var.set("Area: Invalid Input")
                tri_perimeter_var.set("Perimeter: Invalid Input")


        

        notebook.add(frame4, text="Shpe Comp")
        bigger_ar = tk.StringVar(value="Bigger: N/A")
        bigger = tk.StringVar(value="Bigger: N/A")

        choice1 = tk.StringVar()
        choice2 = tk.StringVar()

        tk.Label(frame4, text='Select your shapes to compare:').grid(column=1, row=0)
        ttk.Combobox(frame4, values=["Circle", "Rectangle", "Triangle"], textvariable=choice1).grid(column=1, row=1)
        ttk.Combobox(frame4, values=["Circle", "Rectangle", "Triangle"], textvariable=choice2).grid(column=1, row=2)
        tk.Button(frame4, text='Compare', command=lambda: compare_shapes()).grid(column=1, row=3)
        def compare_shapes():
            tk.Label(frame4, textvariable=bigger_ar).grid(column=1, row=4)
            tk.Label(frame4, textvariable=bigger).grid(column=1, row=5)
            try:
                # Extract numeric values from the StringVars
                if choice1.get() == "Circle":
                    choice1_area = float(circle_area_var.get().split(":")[1].strip())
                    choice1_perimeter = float(circle_perimeter_var.get().split(":")[1].strip())
                elif choice1.get() == "Rectangle":
                    choice1_area = float(rect_area_var.get().split(":")[1].strip())
                    choice1_perimeter = float(rect_perimeter_var.get().split(":")[1].strip())
                elif choice1.get() == "Triangle":
                    choice1_area = float(tri_area_var.get().split(":")[1].strip())
                    choice1_perimeter = float(tri_perimeter_var.get().split(":")[1].strip())

                if choice2.get() == "Circle":
                    choice2_area = float(circle_area_var.get().split(":")[1].strip())
                    choice2_perimeter = float(circle_perimeter_var.get().split(":")[1].strip())
                elif choice2.get() == "Rectangle":
                    choice2_area = float(rect_area_var.get().split(":")[1].strip())
                    choice2_perimeter = float(rect_perimeter_var.get().split(":")[1].strip())
                elif choice2.get() == "Triangle":
                    choice2_area = float(tri_area_var.get().split(":")[1].strip())
                    choice2_perimeter = float(tri_perimeter_var.get().split(":")[1].strip())
            except (ValueError, IndexError):
                # Handle invalid or missing data
                bigger_ar.set("Bigger: Invalid Input")
                bigger.set("Bigger: Invalid Input")
                return

            # Compare areas
            if choice1_area > choice2_area:
                bigger_ar.set(f"Bigger Area: {choice1.get()} ({choice1.get()}: {choice1_area:.2f}, {choice2.get()}: {choice2_area:.2f})")
            elif choice2_area > choice1_area:
                bigger_ar.set(f"Bigger Area: {choice2.get()} ({choice1.get()}: {choice1_area:.2f}, {choice2.get()}: {choice2_area:.2f})")
            else:
                bigger_ar.set(f"Equal Area ({choice1.get()}: {choice1_area:.2f}, {choice2.get()}: {choice2_area:.2f})")

            # Compare perimeters
            if choice1_perimeter > choice2_perimeter:
                bigger.set(f"Bigger Perimeter: {choice1.get()} ({choice1.get()}: {choice1_perimeter:.2f}, {choice2.get()}: {choice2_perimeter:.2f})")
            elif choice2_perimeter > choice1_perimeter:
                bigger.set(f"Bigger Perimeter: {choice2.get()} ({choice1.get()}: {choice1_perimeter:.2f}, {choice2.get()}: {choice2_perimeter:.2f})")
            else:
                bigger.set(f"Equal Perimeter ({choice1.get()}: {choice1_perimeter:.2f}, {choice2.get()}: {choice2_perimeter:.2f})")

        notebook.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.mainloop()

if __name__ == '__main__':
    main(repeat)