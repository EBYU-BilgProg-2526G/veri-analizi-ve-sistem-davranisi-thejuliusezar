
from pathlib import Path 


from src.io_utils import load_signal_csv
from src.analysis import basic_stats, sampling_rate
from src.signal_tools import moving_average
from src.plotting import plot_time




def main():
    path = Path("data") / "sample_signal.csv"
    
    t, x = load_signal_csv(path)
    
    basic_stats(x)
    
    sampling_rate(t)
    
    moving_average(x)
    
    plot_time(t, x, moving_average(x))

if __name__ == "__main__":
    main()

    