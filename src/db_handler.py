import sys
from supabase import create_client, Client
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

PSQL_URL = os.environ.get("PSQL_URL")
PSQL_KEY = os.environ.get("PSQL_KEY")


def get_connection():
    supabase: Client = create_client(PSQL_URL, PSQL_KEY)
    return supabase

def should_exit():
    conn = get_connection()
    DB_NAME = "run_history"
    RUN_ID = "run_id"
    result = conn.table(DB_NAME).select("last_run").eq("id", RUN_ID).execute()
    two_days_ago = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
    if not result.data or result.data[0]["last_run"] < two_days_ago:
        now = datetime.now().strftime("%Y-%m-%d")
        if not result.data:
            conn.table(DB_NAME).insert({"id": RUN_ID, "last_run": now}).execute()
        else:
            conn.table(DB_NAME).update({"last_run": now}).eq("id", RUN_ID).execute()
        sys.exit(1)
    else:
        print(f"Service run recently at {result.data[0]['last_run']}")
        sys.exit(0)
if __name__ == "__main__":
    should_exit()