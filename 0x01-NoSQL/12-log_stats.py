#!/usr/bin/env python3
"""Analyze Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def print_nginx_log_stats(nginx_collection):
    """Prints stats about Nginx request logs."""
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in http_methods:
        method_count = len(list(nginx_collection.find({"method": method})))
        print(f"\tmethod {method}: {method_count}")

    status_requests_count = len(list(
        nginx_collection.find({"method": "GET", "path": "/status"})
    ))
    print(f"{status_requests_count} status check")


def main():
    """Function to gather and display log statistics."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_log_stats(client.logs.nginx)


if __name__ == "__main__":
    main()
