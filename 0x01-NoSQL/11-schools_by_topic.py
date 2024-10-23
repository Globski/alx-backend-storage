#!/usr/bin/env python3
"""Module to retrieve schools by a specific topic from a MongoDB collection."""

def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of schools that contain the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
