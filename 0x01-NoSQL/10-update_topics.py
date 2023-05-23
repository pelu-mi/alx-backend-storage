#!/usr/bin/env python3
""" Python module using mongodb
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """ Change all topics of a document based on the name
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
