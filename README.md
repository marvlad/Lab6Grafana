# After installing prometheus and grafana
# Run the Python scripts. The first script (ReadRawData2PrometheusFormat.py) reads the raw data (raw_log.txt ), and the second script (Expose2Localhost.py) exposes the values. 
# The first script can be run 

# In Terminal 1)
  while true; do python3 ReadRawData2PrometheusFormat.py > raw_file2.txt; sleep 0.5; done

In Terminal 2) 
`python3 Expose2Localhost.py`

In Terminal 3)
`prometheus --config.file=./localdb.yml`


prometheus, by default will shows up in localhost:9090

------grafana----------
You need to start the Grafana service. Example:
brew services start grafana (in Mac, but in Linux will be systemctl)
Grafana will show up in localhost:3000 by default.


# The Lab6-1713058778362.json is a template dashboard generated with Grafana for lab6 use.