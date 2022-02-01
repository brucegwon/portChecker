from threading import Thread


def createThread(func, ipList):
    thread = []

    for ip in ipList:
        th = Thread(target=func, args=(ip,))
        th.start()
        thread.append(th)

    for t in thread:
        t.join()
