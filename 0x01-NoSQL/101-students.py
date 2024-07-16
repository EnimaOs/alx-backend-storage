#!/usr/bin/env python3
"""task adv2"""


def top_students(mongo_collection):
    """
    anything
    """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
