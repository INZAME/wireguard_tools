class Config:
    def __init__(self, get=None):
        self.get = get
        self.config = {'[Interface]': 'Header',
                       'Address': '',
                       'ListenPort': '',
                       'PrivateKey': '',
                       'PostUp': '',
                       'PostDown': ''
                       }
        self.peer = {'\n[Peer]': 'Header',
                     '#': '',
                     'PublicKey': '',
                     'AllowedIPs': ''
                     }
        self.str_config = ''
        self.address = None
        self.name = None

    def create(self, address: str, name, port: int, private_key: str):
        if self.get is not None:
            raise FileExistsError
        self.name = name
        self.address = address
        up, down = self._iptables_rules()
        self.config['Address'] = address
        self.config['ListenPort'] = port
        self.config['PrivateKey'] = private_key
        self.config['PostUp'] = up
        self.config['PostDown'] = down
        self.str_config = self._generate(self.config)

    def add_peer(self, name: str, pub_key: str, ip: str):
        self.peer['#'] = name
        self.peer['PublicKey'] = pub_key
        self.peer['AllowedIPs'] = ip
        peer = self._generate(self.peer)
        if self.get is not None:
            with open(f'./{self.get}', 'a') as cfg:
                cfg.write(peer)
        else:
            self.str_config += peer

    def print(self):
        print(self.str_config)

    def save(self, name: str):
        with open(f'./{name}', 'w') as file:
            file.write(self.str_config)

    def _generate(self, config_dict: dict) -> str:
        string = ''
        for key, value in config_dict.items():
            if value == 'Header':
                string += f'{key}\n'
            elif key == '#':
                string += f'{key} {value}\n'
            else:
                string += f'{key} = {value} \n'
        return string

    def _iptables_rules(self) -> list:
        chars = ('A', 'D')
        rules = []
        for char in chars:
            rules.append(f"iptables -{char} FORWARD -i {self.address} -j ACCEPT; iptables -t nat -{char} POSTROUTING -o {self.name} -j MASQUERADE")
        return rules
