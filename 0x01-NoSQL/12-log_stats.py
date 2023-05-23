#!/usr/bin/env python3
""" Python module using mongodb
"""

import pymongo


def print_nginx_log_stats(mongo_collection):
    """ Return list of school having a specific topic
    """
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    stats_check_count = mongo_collection.count_documents({
                        "method": "GET", "path": "/status"})
    print("{} status check".format(stats_check_count))

if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    print_nginx_log_stats(mongo_collection)
