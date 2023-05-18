import socket
import sys

# socket for establishing network connections
# sys for system-related operations

# Define the target IP range and ports to scan
target_ip_range = ['192.168.0.1', '192.168.0.10']
ports_to_scan = [21, 22, 80, 443]

# Modify these variables to specify your desired IP range and ports.
# Also, if you want to scan a specific port, add it to the ports_to_scan list

# Function to scan ports and identify services
def scan_ports(target_ip, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # socket.AF_INET parameter indicates IPv4 addressing

        # socket.SOCK_STREAM specifies a TCP socket

        # A timeout value of 2 seconds is set to limit the connection attempt

        # Set a timeout value for the connection attempt
        s.settimeout(2)
        # Attempt to establish a connection
        result = s.connect_ex((target_ip, port))

        # method is used to establish a connection to the target IP and port

        # if the connection is successful, the result is 0

        # Check if the port is open, closed, or filtered
        if result == 0:
            print(f"Port {port} is open on {target_ip}")
            # Perform service identification techniques here (e.g., banner grabbing, protocol-specific queries)
            # Identify the service running on the open port
            
            # Add code here to retrieve service information and potential vulnerabilities
            
        elif result == 111:
            print(f"Port {port} on {target_ip} is closed")
        else:
            print(f"Port {port} on {target_ip} is filtered")
        # Close the socket connection
        s.close()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    except socket.error:
        print("Could not connect to the server.")
        sys.exit()

# Function to perform the network scan
def network_scan(ip_range, ports):
    for ip in ip_range:
        print(f"\nScanning IP: {ip}")
        for port in ports:
            scan_ports(ip, port)

def get_service_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner.strip().decide('utf-8')
    except:
        return ''

# Generate the report
def generate_report(ip_range, ports):
    report = {}
    for ip in ip_range:
        open_ports = scan_ports(ip, ports)
        for port in open_ports:
            banner = get_service_banner(ip, port)
            if ip not in report:
                report[ip][port] = banner
    return report
# get_service_banner function takes an IP address and a port as input
# It attempts to establish a connection with the specified IP and port
# if successful, it receives the banner (service identification information) from the remote host.
    # Add code here to generate the detailed report with discovered open ports, services, and vulnerabilities

# Start the network scan
network_scan(target_ip_range, ports_to_scan)

# Generate the report
report = generate_report(target_ip_range, ports_to_scan)

# Print the report
for ip, data in report.items():
    print(f"IP Address: {ip}")
    for port, banner in data.items():
        print(f"Port: {port} - Service: {banner}")

# If the connection is successful (i.e., the port is open), it prints a message indicating that the port is open.

# The script handles potential errors that may occur during the port scanning process.
