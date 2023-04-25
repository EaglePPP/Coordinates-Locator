# Coordinates-Locator
Installation
To use this script, you will need to install the tkinter library using pip. You can install tkinter by running the following command in your terminal:

```pip install tkinter```

Usage
To use the Transparent Window script, simply run the script by typing the following command in your terminal:

```python locator.py```

Once the window is open, click on four different points on the window. After the fourth click, the script will print out the x and y coordinates of the four points that were clicked.

Note that the window is transparent, and you can see through it. You can move the window around and click on any location on your screen.

Customization
You can customize the script to your needs by modifying the values of the following variables in the code:

```self.geometry("1920x1080"):``` The size of the window can be modified by changing the values of the width and height.

```self.attributes("-alpha", 0.3):``` The transparency level of the window can be modified by changing the value of alpha. The value should be between 0 and 1, where 0 is completely transparent and 1 is completely opaque.

```self.title("Transparent Window"):``` The title of the window can be changed by modifying the string inside the parentheses.

```self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", outline="red"):``` The color and size of the points that are displayed on the window after clicking can be modified by changing the values of the fill and outline parameters.
![locator_compress](https://user-images.githubusercontent.com/19349338/234259738-546a3d00-8b53-4631-80eb-f45cf6ee20d7.gif)
