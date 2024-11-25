#!/usr/bin/env/pyhton
import subprocess
import optparse

def input_values():
  reader=optparse.OptionParser()
  reader.add_option("-i","--interface",dest="interface",help="interface name")
  reader.add_option("-m","--mac",dest="new_mac",help="New Mac address")
  (values,keys)= reader.parse_args()

  if not values.interface:
    reader.error("[-] Please enter the interface name or us the --help option.")
  elif not values.new_mac:
    reader.error("[-] Please enter the new mac adddress or use the --help option")
  return values

def change_mac(interface,new_mac):

  print ("changing the mac address of the interface "+ interface + " to " + new_mac)
  subprocess.call(["ifconfig",interface,"down"])
  subprocess.call(["ifconfig",interface,"hw", "ether",new_mac])
  subprocess.call(["ifconfig",interface,"up"])

values=input_values()
change_mac(values.interface,values.new_mac)

