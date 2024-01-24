#!/usr/bin/env python3
"""
Provide advanced stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
Display same as example plus the top 10 most present IPs
"""
from pymongo import MongoClient
from collections import Counter

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """
    Provide advanced stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)

    # Count the occurrences of each IP
    ip_counter = Counter(log['ip'] for log in mongo_collection.find())

    print("IPs:")
    for ip, count in ip_counter.most_common(10):
        print(f"\t{ip}: {count}")

    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017')['logs']['nginx']
    log_stats(nginx_collection)

