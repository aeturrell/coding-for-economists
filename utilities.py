import matplotlib.pyplot as plt
import numpy as np


def really_useful_func(number):
    return number * 10


def default_func():
    print("Script has run")


def test_plot_style():
    plt.style.use("plot_style.txt")
    np.random.seed(402)
    x = np.random.uniform(10, 1e5, 11)
    y = np.random.uniform(10, 1e3, 11)
    fig, ax = plt.subplots()
    ax.set_title("This is a title")
    ax.scatter(
        np.sort(x),
        y,
        s=100,
        zorder=2,
        c=[
            "#bc80bd",
            "#fb8072",
            "#b3de69",
            "#fdb462",
            "#fccde5",
            "#8dd3c7",
            "#ffed6f",
            "#9164c2",
            "#80b1d3",
            "#ccebc5",
            "#b15928",
        ],
        label="legend text",
    )
    x_vals = np.linspace(0.1e5, 1e5, 1000)
    ax.plot(x_vals, x_vals / 1e2, label="more legend text")
    ax.plot(x_vals, x_vals * 0.4 / 1e2 + 10)
    ax.plot(x_vals, -x_vals * 0.4 / 1e2 + 1e3)
    ax.annotate(r"test text $y=e^{\gamma t}$", xy=(1e4, 300))
    ax.legend()
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    plt.show()


if __name__ == "__main__":
    default_func()
