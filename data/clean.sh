#!/bin/bash


cat sys_log | awk -F '-' '{if($9!="[null]" &&$9!="" && $9!="[]"){print $9}}'  | awk 'gsub(/[\[\]]/, "", $0)' > prepare_data
