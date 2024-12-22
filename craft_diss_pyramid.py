import textwrap as txtwrp

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# Plot settings
plt.style.use(
    "https://github.com/aeturrell/coding-for-economists/raw/main/plot_style.txt"
)

labels_diss = ["Replication packet and code", "Paper", "Blog post", "Twitter thread"]
labels_blog = [
    "Take away message and implications",
    "Caveats",
    "Core story",
    "Punchy intro",
    "Inviting title",
]

height = 1
start_x = 0.5
start_y = 0.5
top_y_value = height + start_y
y_positions = np.linspace(
    start_y - height, top_y_value - height + start_y, len(labels_diss)
)
y_positions_blog = np.linspace(
    start_y - height, top_y_value - height + start_y, len(labels_blog)
)
delta_blog = 1.2


def plot_pyramid():
    fig, ax = plt.subplots(figsize=(8, 3), dpi=200)
    # add a Polygon
    diss = mpatches.RegularPolygon(
        xy=[start_x, start_y],
        numVertices=3,
        radius=height,
        alpha=0.4,
        orientation=np.pi,
    )
    base_blog_triangle = 4 * start_x + delta_blog
    blog = mpatches.RegularPolygon(
        xy=[base_blog_triangle, start_y],
        numVertices=3,
        radius=height,
        orientation=np.pi,
        alpha=0.4,
    )
    ax.add_patch(diss)
    ax.add_patch(blog)

    for s, y_pos in zip(labels_diss, y_positions):
        ax.annotate(txtwrp.fill(s, 20), (start_x, y_pos + 0.05), ha="center")

    for s, y_pos in zip(labels_blog, y_positions_blog):
        ax.annotate(txtwrp.fill(s, 20), (base_blog_triangle, y_pos + 0.05), ha="center")

    people_x = -3 * start_x
    detail_x = base_blog_triangle + height + 2 * start_x

    ax.annotate(
        "Fewer people",
        xy=(people_x, -start_y),
        xytext=(people_x, top_y_value - height + 1.5 * start_y),
        arrowprops=dict(arrowstyle="->"),
        ha="center",
        fontsize=10,
    )

    ax.annotate(
        "More detail",
        xy=(detail_x, -start_y),
        xytext=(detail_x, top_y_value - height + 1.5 * start_y),
        arrowprops=dict(arrowstyle="->"),
        ha="center",
        fontsize=10,
    )

    ax.annotate(
        txtwrp.fill("Inverted pyramid of dissemination", 60),
        xy=(0.5 * (people_x + start_x), -height),
        fontsize=12,
        ha="center",
    )

    ax.annotate(
        txtwrp.fill("Typical structure of a blog post", 60),
        xy=(base_blog_triangle * 0.5 + detail_x * 0.5, -height),
        fontsize=12,
        ha="center",
    )

    lims = (-2, 6)
    ax.set_xlim(lims)
    y_size = 1.2
    ax.set_ylim((-y_size, y_size))
    plt.axis("off")
    plt.tight_layout()
    plt.show()
