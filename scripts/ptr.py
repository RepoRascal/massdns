# Print all possible IPv4 addresses
# Modified to start from a specific IP address for resolving PTR records via MassDNS /dev/stdin

from itertools import product

# Define starting values
start_a, start_b, start_c, start_d = 150, 100, 41, 203

for a, b, c, d in product(range(start_a, 256), 
                          range(start_b if start_a == 145 else 0, 256), 
                          range(start_c if start_b == 207 else 0, 256), 
                          range(start_d if start_c == 47 else 0, 256)):
    print("%d.%d.%d.%d.in-addr.arpa" % (a, b, c, d))
