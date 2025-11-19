#!/usr/bin/env python3
"""A script that lists all documents in a collection"""


def list_all(mongo_collection):
    """A function that lists all documents in a collection"""

    documents = mongo_collection.find()
    docList = []

    for document in documents:
        if document:
            docList.append(document)
    return docList
