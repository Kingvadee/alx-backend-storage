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
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        value = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {value}")

    # Use aggregation pipeline to get the top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

    top_ips = list(mongo_collection.aggregate(pipeline))

    print("IPs:")
    for ip_data in top_ips:
        ip = ip_data["_id"]
        count = ip_data["count"]
        print(f"\t{ip}: {count}")



if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017')['logs']['nginx']
    log_stats(nginx_collection)

