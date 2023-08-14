import ipaddress

def count_leading_zeros(binary_string):
    # Remove all the leading zeros and count the difference
    return 32 - len(binary_string.lstrip('0'))


def get_minimal_spanning_subnet(ip_list):
    if not len(ip_list) >= 2:
        print("Please provide at least 2 IP addresses\nExiting...\n")
        exit(1)
    
    # Step 1: convert IPs to integers and find the min / max
    print("\nStep 1: Narrowing down the problem by finding the min/max IPs")
    int_ips = [int(ipaddress.IPv4Address(ip)) for ip in ip_list]
    min_ip = min(int_ips)
    max_ip = max(int_ips)

    print_ip_line_from_int(min_ip,"(min)")
    print_ip_line_from_int(max_ip,"(max)")


    # Step 2: find the differing bits using XOR (^):
    print("\nStep 2: locate different bits with XOR (1=different)")
    diff_bits = min_ip ^ max_ip
    diff_bits_str = bin(diff_bits)[2:].zfill(32)
    print(f"{diff_bits_str}")


    # Step 3: find the common prefix of min/max (leading zeros of "diff_bits")
    print("\nStep 3: find common prefix (leading zeros of the XOR result)")
    lzeros = count_leading_zeros(diff_bits_str)
    print(f"{diff_bits_str}")
    print("^".rjust(lzeros)+f" {lzeros} found")


    # Step 4: calculate subnet mask based on the common prefix length and then the subnet
    print("\nStep 4: find subnet mask, apply it to min IP")
    subent_mask = (0xFFFFFFFF << (32 - lzeros)) # shift left to keep (lzeros) 1s and (32-lzeros) 0s
    subnet_mask_str = bin(subent_mask)[-32:] # keep only the last 32 bits after the shift
    network_address = min_ip & subent_mask # bitwise AND

    print_ip_line_from_int(min_ip,"(min)")
    print_ip_line_from_int(int(subnet_mask_str,2),"(subnet mask)")
    print_ip_line_from_int(network_address, "(network address)")


    # Step 5: result
    print("\nStep 5: Result")
    subnet = str(ipaddress.IPv4Address(network_address)) + '/' + str(lzeros)
    return subnet




# takes  : (string) IP in dotted-decimal notation
# returns: (string) binary string of the IP prefixed with “0b”
#
# example:
#   in:  "192.168.0.0"
#   out: "0b110000001010100000"
#
def ddn_to_bin(ip):
    return bin(int(ipaddress.IPv4Address(ip)))


# same as ddn_to_bin()
# but fills leading zeros if needed to reach 32 characters (an IP has 32 bits) 
#
def ddn_to_bin_32(ip):
    return ddn_to_bin(ip)[2:].zfill(32)


# takes  : (int) number
# returns: (string) binary string with 32 characters, NOT prefixed with “0b”
#
# example:
#   in:  197280
#   out: "110000001010100000"
#
def int_to_bin_32(ip):
    return bin(ip)[2:].zfill(32)


# takes  : (string) IP in dotted-decimal notation
# returns: (int)    the integer number we get by transforming the IP's 32 bits to decimal format
#
# example:
#   in:  "192.168.0.0"
#   out: 197280
#
def ddn_to_int(ip):
    return int(ddn_to_bin(ip),2)


# takes : (string) IP in dotted-decimal notation
# prints: a line with 3 columns:
#         IP (binary)    IP (dotted-decimal notation)    IP (integer)
#
def print_ip_line(ip):
    print(f"{ddn_to_bin_32(ip)}    {ip:23}    {int(ddn_to_int(ip)):10}")


# takes : (int) IP, (string) a comment to be printed
# prints: a line with 4 columns:
#         IP (binary)    IP (dotted-decimal notation)    IP (integer)    (comment)
# 
def print_ip_line_from_int(num, comment):
    print(f"{int_to_bin_32(num)}    {str(ipaddress.IPv4Address(num)):23}    {num:10}    {comment}")


def print_header_info(ip_list):
    print("Provided list of IPs:")
    col_a = "Binary"
    col_b = "Dotted-decimal notation"
    col_c = "int"
    col_d = "Comments"

    print(f"{col_a:32}    {col_b:15}    {col_c:10}    {col_d:20}")
    for ip in ip_list: print_ip_line(ip)
    print("--------------------------------------------------------------------------------------------")




# Examples
# ip_list = ['192.168.0.0','192.168.0.3']
# ip_list = ['192.168.0.0','192.168.0.4']
# ip_list = ['192.168.0.4','192.168.0.7']
# ip_list = ['192.168.0.0','192.168.0.7']
# ip_list = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.63']
# ip_list = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.64']
ip_list = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.127']
# ip_list = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.128']
# ip_list = ['192.168.0.0','192.168.1.0']
# ip_list = ['192.168.0.0','192.168.1.0','192.168.2.0']
# ip_list = ['192.168.0.0','192.168.1.0','192.168.255.0']
# ip_list = ['10.0.0.1','192.168.0.0']
# ip_list = ['10.0.0.0','63.0.0.0']
# ip_list = ['10.0.0.0','127.0.0.0']
# ip_list = ['10.0.0.0','128.0.0.0']



# print IP list and final result after calculating it:
print_header_info(ip_list)
print(get_minimal_spanning_subnet(ip_list))

