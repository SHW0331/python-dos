# pip install pandas
# pip install pandas openpyxl
import pandas as pd

log_data = pd.read_csv('/var/log/snort/snort.log', delimiter=',')
