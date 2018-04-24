import nfc


CONNECTION_TYPE = 'usb'


def connected(llc):
    print('connected!')
    return True


with nfc.ContactlessFrontend(CONNECTION_TYPE) as clf:
    clf.connect(llcp={'on-connect': connected})
