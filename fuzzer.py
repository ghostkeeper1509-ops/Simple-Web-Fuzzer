#!/usr/bin/env python3
import requests
import sys

print("-" * 50)
print(" Simple Python Web Directory Fuzzer")
print("-" * 50)

# Target URL input (e.g., http://testphp.vulnweb.com)
target_url = input("Enter target URL (e.g., http://example.com): ")

# A small built-in list of common directories/files to test
common_directories = ["admin", "login", "dashboard", "robots.txt", "config.bak", "uploads", "test"]

print(f"\n[+] Starting scan on: {target_url}")
print("-" * 50)

try:
    for directory in common_directories:
        full_url = f"{target_url}/{directory}"
        response = requests.get(full_url)
        
        # If status code is 200, the page exists!
        if response.status_code == 200:
            print(f"[FOUND] {full_url} (Status: 200)")
        elif response.status_code == 403:
            print(f"[FORBIDDEN] {full_url} (Status: 403)")

except requests.exceptions.MissingSchema:
    print("\n[-] Error: Please include http:// or https:// in your URL.")
    sys.exit()
except requests.exceptions.ConnectionError:
    print("\n[-] Error: Could not connect to the target server.")
    sys.exit()

print("-" * 50)
print("Scan completed!")
