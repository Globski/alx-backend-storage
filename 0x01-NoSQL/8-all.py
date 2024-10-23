#!/usr/bin/env python3
"""Module to list all documents in a MongoDB collection."""
from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents, or an empty list if no documents are found.
    """
    return list(mongo_collection.find())
