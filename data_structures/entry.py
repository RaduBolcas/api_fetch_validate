import ipaddress

from datetime import datetime


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = bool(available)
        self.last_used = datetime.strptime(last_used, "%d/%m/%y %H:%M:%S")

    def __lt__(self, other):
        return ipaddress.IPv4Address(self.address) < ipaddress.IPv4Address(other.address)

    def __le__(self, other):
        return ipaddress.IPv4Address(self.address) <= ipaddress.IPv4Address(other.address)

    def __ge__(self, other):
        return ipaddress.IPv4Address(self.address) >= ipaddress.IPv4Address(other.address)

    def __gt__(self, other):
        return ipaddress.IPv4Address(self.address) > ipaddress.IPv4Address(other.address)

    def __eq__(self, other):
        return self.address == other.address

    def __ne__(self, other):
        return self.address != other.address
