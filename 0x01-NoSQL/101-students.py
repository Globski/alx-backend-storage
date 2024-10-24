#!/usr/bin/env python3


def top_students(mongo_collection):
    """Return all students sorted by average score."""
    students = list(mongo_collection.find())
    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        student['averageScore'] = sum(scores) / len(scores) if scores else 0

    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
