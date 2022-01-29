import unittest

from data_structures.datacenter import Datacenter
from data_structures.network_collection import NetworkCollection


class TestDataCenter(unittest.TestCase):
    def test_remove_invalid_clusters_keeps_location_name_w_only_three_letters(self):
        cluster_dict = {
            "BER-1": {"security_level": 5,
                      "networks": {}
                      },
            "BER-203": {"security_level": 5,
                        "networks": {}
                        },
            "BE-1": {"security_level": 5,
                     "networks": {}
                     },
            "TEST-1": {"security_level": 5,
                       "networks": {}
                       },
            "XBER-1": {"security_level": 5,
                       "networks": {}
                       },
            "BERX-1": {"security_level": 5,
                       "networks": {}
                       },
            "-1": {"security_level": 5,
                   "networks": {}
                   },
        }
        name = "Berlin"
        expected_result = ['BER-1', "BER-203"]
        self.data_center = Datacenter(name, cluster_dict)
        self.data_center.remove_invalid_clusters()
        result = [cluster.name for cluster in self.data_center.clusters]
        self.assertEqual(expected_result, result)

    def test_remove_invalid_clusters_keeps_location_name_w_one_to_three_numbers(self):
        cluster_dict = {
            "BER-1": {"security_level": 5,
                      "networks": {}
                      },
            "BER-": {"security_level": 5,
                     "networks": {}
                     },

            "BER-4000": {"security_level": 5,
                         "networks": {}
                         },
        }
        name = "Berlin"
        expected_result = ['BER-1']
        self.data_center = Datacenter(name, cluster_dict)
        self.data_center.remove_invalid_clusters()
        result = [cluster.name for cluster in self.data_center.clusters]
        self.assertEqual(expected_result, result)

    def test_remove_invalid_clusters_keeps_location_name_w_uppercase_letters(self):
        cluster_dict = {
            "BER-1": {"security_level": 5,
                      "networks": {}
                      },
            "ber-1": {"security_level": 5,
                      "networks": {}
                      }
        }
        name = "Berlin"
        expected_result = ['BER-1']
        self.data_center = Datacenter(name, cluster_dict)
        self.data_center.remove_invalid_clusters()
        result = [cluster.name for cluster in self.data_center.clusters]
        self.assertEqual(expected_result, result)

    def test_remove_invalid_clusters_keeps_location_name_that_starts_with_correct_letters(self):
        cluster_dict = {
            "BER-1": {"security_level": 5,
                      "networks": {}
                      },
            "TEST-1": {"security_level": 5,
                       "networks": {}
                       },
            "XBER-1": {"security_level": 5,
                       "networks": {}
                       },
            "BERX-1": {"security_level": 5,
                       "networks": {}
                       },
        }
        name = "Berlin"
        expected_result = ['BER-1']
        self.data_center = Datacenter(name, cluster_dict)
        self.data_center.remove_invalid_clusters()
        result = [cluster.name for cluster in self.data_center.clusters]
        self.assertEqual(expected_result, result)


class TestNetworkCollection(unittest.TestCase):
    def test_remove_invalid_records_keeps_entries_w_correct_subnet(self):
        raw_entry_list = [
            {'address': '255.255.255.0', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.167.255.255', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.0', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.1', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.4', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0.255', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.1.1', 'available': True, 'last_used': '30/01/20 17:00:00'}
        ]
        address = "192.168.0.0/24"
        expected_result = ['192.168.0.0', '192.168.0.1', '192.168.0.4', '192.168.0.255']

        self.network_collection = NetworkCollection(address, raw_entry_list)
        self.network_collection.remove_invalid_records()
        result = [entry.address for entry in self.network_collection.entries]
        self.assertEqual(expected_result, result)

    def test_remove_invalid_records_keeps_entries_w_valid_ip_addresses(self):
        raw_entry_list = [
            {'address': None, 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': True, 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': 5, 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': "random_string", 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168..0.3', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0.3.', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0', 'available': False, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0.288', 'available': False, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0.1', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.2', 'available': False, 'last_used': '30/01/20 17:00:00'},
        ]

        address = "192.168.0.0/24"
        expected_result = ['192.168.0.1', '192.168.0.2']

        self.network_collection = NetworkCollection(address, raw_entry_list)
        self.network_collection.remove_invalid_records()
        result = [entry.address for entry in self.network_collection.entries]
        self.assertEqual(expected_result, result)

    def test_remove_invalid_records_keeps_entries_w_valid_ipv4_addresses(self):
        raw_entry_list = [
            {'address': '192.168.0.1', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.2', 'available': False, 'last_used': '30/01/20 17:00:00'},
            {'address': '2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '2001:db8::8a2e:370:7334', 'available': True, 'last_used': '30/01/20 17:00:00'}
        ]

        address = "192.168.0.0/24"
        expected_result = ['192.168.0.1', '192.168.0.2']

        self.network_collection = NetworkCollection(address, raw_entry_list)
        self.network_collection.remove_invalid_records()
        result = [entry.address for entry in self.network_collection.entries]
        self.assertEqual(expected_result, result)

    def test_sort_records(self):
        raw_entry_list = [
            {'address': '192.168.1.1', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.0', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.255', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.168.0.4', 'available': True, 'last_used': '30/01/20 17:00:00'},
            {'address': '192.168.0.1', 'available': False, 'last_used': '30/01/20 16:00:00'},
            {'address': '192.167.0.1', 'available': False, 'last_used': '30/01/20 16:00:00'},

        ]
        address = "192.168.0.0/16"
        expected_result = ['192.167.0.1', '192.168.0.0', '192.168.0.1', '192.168.0.4', '192.168.0.255', '192.168.1.1']

        self.network_collection = NetworkCollection(address, raw_entry_list)
        self.network_collection.sort_records()
        result = [entry.address for entry in self.network_collection.entries]
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
