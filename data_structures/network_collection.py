import ipaddress

from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipaddress.IPv4Network(ipv4_network)
        self.raw_entry_list = raw_entry_list
        self.entries = []
        for entry in raw_entry_list:
            self.entries.append(Entry(address=entry["address"], available=entry["available"],
                                      last_used=entry["last_used"]))

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        entries = self.entries.copy()
        for entry in entries:
            try:
                ip = ipaddress.ip_address(entry.address)
                if ip not in self.ipv4_network:
                    raise ValueError
            except ValueError:
                self.entries.remove(entry)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
