with open('/etc/passwd') as fh:
    for line in fh:
        uid=line.split(':')
        if int(uid[2]) > 500:
            print("User: {} - UID: {}".format(uid[0],uid[2]))

