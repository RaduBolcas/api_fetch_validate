import re

from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.cluster_dict = cluster_dict
        self.clusters = []
        for location_name, cluster_values in self.cluster_dict.items():
            self.clusters.append(Cluster(name=location_name, network_dict=cluster_values["networks"],
                                         security_level=cluster_values["security_level"]))

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        clusters = self.clusters.copy()
        for cluster in clusters:
            matched = re.match(self.name[:3].upper() + "-[0-9]{1,3}$", cluster.name)
            if not matched:
                self.clusters.remove(cluster)



