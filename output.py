#!/usr/bin/env python

import yaml
import json 
from pprint import pprint as pp

#setup example list
def generate_list():
	mylist = []
	my_list = range (8)
	my_list.append('test')
	my_list.append('stuff')
	my_list.append({})
	my_list[-1]['ip'] = '10.10.1.1'
	my_list[-1]['dev'] = 'router'
	#print my_list
	return my_list

#convert list to json and yaml formats and output with filename file_name
def output_files(file_name,my_list):
	with open(file_name + ".yml", "w") as f:
		f.write(yaml.dump(my_list, default_flow_style=False))
	with open(file_name + ".json", "w") as f:
		f.write(json.dumps(my_list))

#read json file
def read_json_file(json_file):
	with open(json_file, "r") as f:
		return json.load(f)

#read yaml file
def read_yaml_file(yaml_file):
	with open(yaml_file, "r") as f:
		return yaml.load(f)

#test functions and produce output
file_name = "testfile"
output_files(file_name,generate_list())
pp(read_json_file(file_name + ".json"))
pp(read_yaml_file(file_name + ".yml"))
