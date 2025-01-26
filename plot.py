# plot.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def plot_costs(results, canvas):
    cost_components = ["Construction Cost", "Maintenance Cost", "Repair Cost", "Demolition Cost",
                       "Environmental Cost", "Social Cost", "User Cost"]

    steel_costs = [results[0][i + 1] for i in range(len(cost_components))]
    concrete_costs = [results[1][i + 1] for i in range(len(cost_components))]

    figure = plt.figure()
    ax = figure.add_subplot(111)

    x = range(len(cost_components))
    bar_width = 0.35

    ax.bar(x, steel_costs, width=bar_width, label="Steel", color="blue")
    ax.bar([p + bar_width for p in x], concrete_costs, width=bar_width, label="Concrete", color="orange")

    ax.set_xticks([p + bar_width / 2 for p in x])
    ax.set_xticklabels(cost_components, rotation=45, ha="right")
    ax.set_ylabel("Cost (₹)")
    ax.set_title("Cost Comparison: Steel vs. Concrete")
    ax.legend()

    canvas.figure = figure
    canvas.draw()
