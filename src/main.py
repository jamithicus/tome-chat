import EchoBot

if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    _password = getpass.getpass
    xmpp = EchoBot('jamithicus@xmpp.jp', _password)

    xmpp.connect()
    xmpp.process(block=True)
