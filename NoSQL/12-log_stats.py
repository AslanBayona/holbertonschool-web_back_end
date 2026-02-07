#!/usr/bin/env python3
""" 12. Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Total de logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Métodos (IMPORTANTE: Tabulación \t)
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status Check (IMPORTANTE: method=GET Y path=/status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
