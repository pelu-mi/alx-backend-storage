#!/usr/bin/env python3
""" Python module using mongodb
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Return list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
