import os
import sys


def getIpList(filename):

    # Check file exists.
    if os.path.isfile(filename):
        pass
    else:
        print("* ERROR: Can't find IP List file. Check file name please.")
        sys.exit()

    with open(filename, 'r') as f:
        ipList = f.readlines()
        ipList = [ip.rstrip('\n') for ip in ipList]
        return ipList


def ipValid(ipList):

    for ip in ipList:
        seg = ip.split('.')
        if len(seg) == 4 and int(seg[0]) > 0 and int(seg[0]) < 255 and int(seg[1]) >= 0 and int(seg[1]) < 255 and int(seg[2]) >= 0 and int(seg[2]) < 255 and int(seg[3]) >= 0 and int(seg[3]) < 255:
            pass
        else:
            print(f"* Error: {ip} is not valid")
            sys.exit()


if __name__ == "__main__":
    ips = getIpList("ip.txt")
    print(ips)
