import socket

# Input and output file paths
input_file_path = r'C:\Users\a_hettprab1\Desktop\nslookup script\ip_addresses.txt'
output_file_path = r'C:\Users\a_hettprab1\Desktop\nslookup script\nslookups.txt'

# Function to perform DNS lookup
def resolve_ip_to_dns(ip_address):
    try:
        return ip_address + " : " + socket.gethostbyaddr(ip_address)[0] + '\n'
    except socket.herror:
        return ip_address + " : " + "DNS resolution failed" + '\n'

# Reading IP addresses from the file
with open(input_file_path, 'r') as input_file:
    ip_addresses = input_file.readlines()

# Resolving IP addresses and writing to the output file
with open(output_file_path, 'w') as output_file:
    for ip_address in ip_addresses:
        result = resolve_ip_to_dns(ip_address.strip())
        output_file.write(result)
        print(result.strip())
