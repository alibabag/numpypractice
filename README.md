# Matplotlib Examples

This repository contains examples of using Matplotlib for data visualization in Python. The examples include various types of plots such as line plots, stack plots, pie charts, and more. The repository also includes a CSV file with NBA player data.

## Files

- `basics-matplotlib.py`: Contains basic examples of creating plots using Matplotlib.
- `figure.py`: Contains examples of creating figures and subplots using Matplotlib.
- `graphs.py`: Contains examples of creating stack plots, pie charts, bar charts, and histograms using Matplotlib.
- `nba.csv`: A CSV file containing data about NBA players.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/matplotlib-examples.git
    cd matplotlib-examples
    ```

2. Install the required libraries:
    ```sh
    pip install matplotlib numpy pandas
    ```
    or it could be pip3 install matplotlib numpy pandas


    
3. Run the Python scripts to see the plots:
    ```sh
    python basics-matplotlib.py
    python figure.py
    python graphs.py
    ```

## Examples

### Line Plot

Example of a line plot from `basics-matplotlib.py`:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear', color="red")
plt.plot(x, x**2, label='quadratic', color="blue")
plt.plot(x, x**3, label='cubic', color="green")
plt.title('My first plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend(loc="upper left")
plt.show()


## Note

Please note that all buttons and labels on the site are written in Turkish.