
import matplotlib
import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    
    plt.plot(t, x_raw, label = "Ham")
    plt.plot(t, x_filt, "r-", label = "Filtrelenmiş")
    plt.title("Zaman-Sinyal Grafiği"),
    plt.xlabel("Zaman")
    plt.ylabel("Sinyal")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("time_signal.png", dpi = 300)

