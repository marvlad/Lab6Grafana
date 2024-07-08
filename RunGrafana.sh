#!/bin/bash

sshf_pi(){
	sshfs $1:/home/pi/LAPPD_DAQ/LocalLogs logs
}

run_prometheus(){
	prometheus --config.file=./localdb.yml &
}

expose_metrics(){
	python3 Expose2Localhost.py &
}

update_file(){
	while true; do python3 ReadRawData2PrometheusFormat.py > raw_file2.txt; sleep 0.4; done
}

run(){
	#sshf_pi
	run_prometheus
	expose_metrics
	update_file
}
