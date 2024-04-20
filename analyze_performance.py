
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def compute_average_metrics(df):
    avg_sent = df['Data Sent (bytes)'].mean()
    avg_received = df['Data Received (bytes)'].mean()
    avg_energy = df['Energy Consumption (mJ)'].mean()
    return avg_sent, avg_received, avg_energy

def main():
    data_path = 'data_consumption_metrics.csv'
    data = load_data(data_path)
    average_sent, average_received, average_energy = compute_average_metrics(data)
    print(f'Average Data Sent: {average_sent} bytes')
    print(f'Average Data Received: {average_received} bytes')
    print(f'Average Energy Consumption: {average_energy} mJ')

if __name__ == '__main__':
    main()
