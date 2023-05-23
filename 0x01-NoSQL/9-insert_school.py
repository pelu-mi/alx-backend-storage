#!/usr/bin/env python3
""" Python module using mongodb
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Insert document into collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
