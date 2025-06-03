#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Obyekti JSON formatında fayla yazır"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
