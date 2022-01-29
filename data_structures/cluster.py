from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = security_level
        self.networks = []
        for ipv4_network, entry_list in network_dict.items():
            self.networks.append(NetworkCollection(ipv4_network=ipv4_network, raw_entry_list=entry_list))


