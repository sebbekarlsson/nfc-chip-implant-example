# nfc-chip-implant-example
> Example on how to trigger an action when implant is nearby

<img src='my-implant.jpg' width='250px'/>

## Requirements
> You will need to install:

* nfcpy

## Example:
> [__main__\.py](__main__\.py)

    import nfc


    CONNECTION_TYPE = 'usb'


    def connected(llc):
        print('connected!')
        return True


    with nfc.ContactlessFrontend(CONNECTION_TYPE) as clf:
        clf.connect(llcp={'on-connect': connected})     
