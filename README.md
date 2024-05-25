# PyScripts and Prometheus

After installing Prometheus and Grafana run the Python scripts. In three terminals run the following 

Terminal 1:
```javascript
while true; do python3 ReadRawData2PrometheusFormat.py > raw_file2.txt; sleep 0.5; done
```

Terminal 2:
```javascript
python3 Expose2Localhost.py
```

Terminal 3:
```javascript
prometheus --config.file=./localdb.yml
```

The first script (`ReadRawData2PrometheusFormat.py`) reads the raw data (`raw_log.txt`), and the second script (`Expose2Localhost.py`) exposes the values. Prometheus, by default, will show up in `localhost:9090`


# Grafana
Start the Grafana service. Example:

`brew services start grafana` (in Mac, but in Linux will be `systemctl`)

Grafana will show up in `localhost:3000` by default.


The `Lab6-1713058778362.json` is a template dashboard generated with Grafana for lab6 use.
