# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import BridgeCostApp
from calculations import init_database, calculate_costs
from plot import plot_costs
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def main():
    app = QApplication(sys.argv)

    conn, cursor = init_database()

    window = BridgeCostApp(calculate_costs=lambda span, width, traffic, life: calculate_costs(cursor, span, width, traffic, life),
                           plot_costs=lambda results: plot_costs(results, canvas=window.canvas))

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
