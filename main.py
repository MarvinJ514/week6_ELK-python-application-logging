import logging
import logstash
import sys
import time
import system_query
import PySimpleGUI
import pint 
import psutil
import platform

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.DEBUG)
test_logger.addHandler(logstash.LogstashHandler('18.206.45.152', 5959, version=1))

system_info = system_query.query_all()
system_info2 = platform.platform()
cpu_info = platform.processor()
machine_info = platform.machine()
ram_info = str(((system_info['ram'])['total'])/(1024*1024*1024))

#For testing purposes
test_logger.info(system_info['host'])
test_logger.info(system_info2)
test_logger.info(machine_info)
test_logger.info(cpu_info)
test_logger.info(((system_info['ram'])['total'])/(1024*1024*1024))
test_logger.debug('Application executed successfully')

PySimpleGUI.theme('DarkAmber')
layout = [
    [PySimpleGUI.Text('Hostname = ' + system_info['host'])],
    [PySimpleGUI.Text('OS = ' + system_info['os'])],
    [PySimpleGUI.Text('Platform = ' + machine_info)],
    [PySimpleGUI.Text('CPU = ' + cpu_info)],
    [PySimpleGUI.Text('Available RAM = ' + ram_info)],
    [PySimpleGUI.SimpleButton('OK')]]

window = PySimpleGUI.Window('System Info', layout)

while True:
    event = window.read()
    if event in (None,'OK'):
        break
    exit()

window.close()





