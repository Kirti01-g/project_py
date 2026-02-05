import ipywidgets as widgets
from IPython.display import display

# Example 1: An interactive slider
def f(x):
    print(x)

slider = widgets.IntSlider(min=0, max=10, step=1, description='Value:')
display(slider)

# To link the slider to a function
widgets.interactive(f, x=slider);

# Example 2: A simple button and output
button = widgets.Button(description='Click Me!')
output = widgets.Output()

def on_button_clicked(b):
    with output:
        print('Button clicked!')

button.on_click(on_button_clicked)
display(button, output)
