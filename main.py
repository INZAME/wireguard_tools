from tools import Config


def main():
    config = Config('mycfg2.cfg')
    # config.create('192.168.8.1', 'eth0', 125625, 'ASDA5D5A2AS15D1AS61D61A6D')
    # config.add_peer('my_pc', 'SSD5ASD25C25XV4FGGDC6', '192.168.8.2' )
    config.add_peer('third', 'IWMKJHJ4FGGD25C25XV', '192.168.8.4')
    # config.save('mycfg.cfg')


if __name__ == '__main__':
    main()
