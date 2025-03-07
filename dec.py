import re
hex_data = open("./lua.txt", "r").read()

# Convert to binary
binary_data = bytes.fromhex(hex_data)

# Write to file
with open("luabytecode.luac", "wb") as f:
    f.write(binary_data)
