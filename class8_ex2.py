#!/usr/bin/env python

import show_version
import sys

def process_show_version (file_to_process):
	print "model:			",show_version.function3.obtain_model(file_to_process)
	print "os_version:		",show_version.function1.obtain_os_version(file_to_process)
	print "uptime:			",show_version.function2.obtain_os_uptime(file_to_process)


file_to_process = sys.argv.pop()

process_show_version(file_to_process)
