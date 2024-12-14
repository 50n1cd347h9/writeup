compared = "xjagpediegzqlnaudqfwyncpvkqneusycourkguerjpzcbstcc"
new = [ord(i) for i in compared]
old = [i for i in new]

key0 = 0x55
key1 = 0x33
key2 = 0xf
key3 = 0x61

q = 0

# new[j] = key3 + ((e_1 >> 4 & key2) + old[j] - key3 + (key2 & e_1)) % 0x1a
# new[j] - key3 == ((e_1 >> 4 & key2) + old[j] - key3 + (key2 & e_1)) % 0x1a
# (e_1 >> 4 & key2) + old[j] + (key2 & e_1) == 0x1a * q + new[j]
# old[j] == 0x1a * q + new[j] - (key2 & e_1) - (e_1 >> 4 & key2)

for i in range(0, 3):
    for j in range(0, len(compared)):
        e_0 = ((j % 0xff) >> 1 & key0) + ((j % 0xff) & key0)
        e_1 = ((e_0 >> 2) & key1) + (key1 & e_0)

        old[j] = 0x1a * q + new[j] - (key2 & e_1) - (e_1 >> 4 & key2)

    new = old

print(''.join([chr(i) for i in old]))
