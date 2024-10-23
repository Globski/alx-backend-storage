#!/usr/bin/env python3
"""Module to insert a new document in a MongoDB collection."""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The document attributes to insert.

    Returns:
        The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
