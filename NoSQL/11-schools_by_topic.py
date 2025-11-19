#!/usr/bin/env python3
"""A script that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """A function that queries information from document"""

    return list(mongo_collection.find({"topics": topic}))
