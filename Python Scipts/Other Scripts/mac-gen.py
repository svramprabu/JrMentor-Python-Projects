#it4min
f = open("mac.txt", "a")
mac = '00:00:00:'
for number in range(16**6):
    hex_num = hex(number)[2:].zfill(6)
    mact = "{}{}{}:{}{}:{}{}".format(mac,*hex_num)
    f.write(mact+'\n')
    print (mact)
f.close()