import rrdtool
import matplotlib.pyplot as plt

def plot_rrd_graph(rrd_file, output_file):
    start_time = "end-1h"
    end_time = "now"
    graph_title = "CPU Usage"
    
    graph_data = rrdtool.fetch(rrd_file, "AVERAGE",
                               "--start", start_time,
                               "--end", end_time)

    values = graph_data[2]
    interval = int((graph_data[0][1] - graph_data[0][0]) * 5)
    num_records = len(values)
    start_timestamp = graph_data[0][0]

    times = [start_timestamp + i * interval for i in range(num_records)]

    plt.plot(times, values, color='red')
    plt.title(graph_title)
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.grid(True)
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    rrd_file = "cpu_info.rrd"
    output_file = "cpu_info_graph.png"
    plot_rrd_graph(rrd_file, output_file)
