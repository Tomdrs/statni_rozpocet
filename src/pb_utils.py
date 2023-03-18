from pocketbase import PocketBase
import os

def fetch_all_for_table(name):
    client = PocketBase(os.environ["POCKETBASE_URL"])

    full_list = client.records.get_full_list(name, 200, {"sort": "-created"})

    return full_list
