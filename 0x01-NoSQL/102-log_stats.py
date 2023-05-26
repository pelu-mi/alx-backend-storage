#!/usr/bin/env python3
""" Python module using mongodb
"""

from pymongo import MongoClient


def print_nginx_log_stats(mongo_collection):
    """ Provides some stats from nginx logs
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


def print_sorted_top_ips(mongo_collection):
    """ Print out the sorted top 10 most present IPs in the logs
    """
    print("IPs:")
    request_ips = mongo_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "totalRequests": {"$sum": 1}
            }
        },
        {
            "$sort": {"totalRequests": -1}
        },
        {
            "$limit": 10
        }
    ])
    for request_ip in request_ips:
        ip = request_ip["_id"]
        ip_count = request_ip["totalRequests"]
        print("\t{}: {}".format(ip, ip_count))


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    print_nginx_log_stats(mongo_collection)
    print_sorted_top_ips(mongo_collection)
