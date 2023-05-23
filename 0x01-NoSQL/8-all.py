#!/usr/bin/env python3
""" Python module using mongodb
"""

import pymongo


def list_all(mongo_collection):
    """ List all document in a collection
    """
    return [doc for doc in mongo_collection.find()]
