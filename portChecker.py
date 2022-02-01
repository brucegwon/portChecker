from pkg.getIpList import getIpList, ipValid
from pkg.checkConnect import checkConnect
from pkg.createThread import createThread

ipList = getIpList("files/ip.txt")

ipValid(ipList)

createThread(checkConnect, ipList)
