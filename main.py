# imports
import re

# Regular expression
ip_regex = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")


# Enter an IP address
print("Enter an IP address")
ipAddr = input()
# Check if valid
if not re.search (ip_regex, ipAddr):
    print("Invalid IP address")
    quit()

# print ("You entered " + ipAddr)

# Enter CIDR notation
print("Enter CIDR subnet mask")
ipCidr = int(input())
# Check if valid
cidrRange = 0 <= ipCidr <= 32
if not cidrRange:
    print("Invalid CIDR")
    quit()
# function for calculating subnet class and subnet mask
# Class A (1-126), 255.0.0.0
# Class B (128-191), 255.255.0.0
# Class C (192-223), 255.255.255.0

# Function for calculating each subnet mask octet
def subOctet(ipCidr):
    i = 0
    j = ipCidr
    n = 7
    octet = 0
    while i < j:
        octet = octet + 2**n
        i += 1
        n -= 1
    return octet

#print(subOctet(ipCidr))


# Get subnet mask from cidr
subMaskOne = 0
subMaskTwo = 0
subMaskThree = 0
subMaskFour = 0

# First octet
if ipCidr >= 8:
    subMaskOne = 255
else: subMaskOne = subOctet(ipCidr)

# Second octet
octTwo = 0
if ipCidr > 8 and ipCidr <= 16:
    octTwo = ipCidr - 8
elif ipCidr > 16:
    octTwo = 8
else: pass
subMaskTwo = subOctet(octTwo)

# Third octet
octThree = 0
if ipCidr > 16 and ipCidr <= 24:
    octThree = ipCidr - 16
elif ipCidr > 24:
    octThree = 8
else: pass
subMaskThree = subOctet(octThree)

# Fourth octet
octFour = 0
if ipCidr > 24:
    octFour = ipCidr - 24
else: pass
subMaskFour = subOctet(octFour)


# Print subnet mask
# print("Subnet Mask: " + subMaskOne + "." + subMaskTwo + "." + subMaskThree + "." + subMaskFour)
print("Subnet Mask: " + "%s.%s.%s.%s" % (subMaskOne, subMaskTwo, subMaskThree, subMaskFour))


# function for calculating subnet network address and first host address
# Network values are on left, Host values are on right
# Network address: Set all host bits to 0 (ex: 10.0.0.0)
# First Host address: add one to netwrok address (ex: 10.0.0.1)

# function for calculating Network broadcast address
# Set all host bits to 1 (in binary) ex: 10.255.255.255

# function for calculating last usable IP address
# Subract 1 from Broadcast address.

# Other
# Check for loopback address (127.0.0.0/8)