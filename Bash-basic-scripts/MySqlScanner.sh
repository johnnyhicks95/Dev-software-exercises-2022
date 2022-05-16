# Nmap looking for sql ports
#! /bin/bash
echo "Enter the starting IP address:"
read FirstIP
echo "Enter the last octet of the last IP address:"
read LastOctetIp
echo "Enter the port number you want to scan for:"
read port

# executing nmap
nmap -sP $FirstIP -$LastOctetIp -p $port >/dev/null -oG MySQLscan
cat MySQLscan | grep open > MySQLscan2
cat MySQLscan2

times
# close execution
exit

