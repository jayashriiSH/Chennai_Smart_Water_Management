import random
import time
from datetime import datetime
from supabase import create_client

supabase = create_client(
    "https://dstilpwjehgsfgbuakjf.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRzdGlscHdqZWhnc2ZnYnVha2pmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2ODc1NTA2NywiZXhwIjoyMDg0MzMxMDY3fQ.SNwYXUXV4GwFZFYAS4seKMaIXxKWcHlZMJabUTGKsc0"

)

pipes = {
    "Anna Nagar": ["P101", "P102"],
    "T Nagar": ["P201", "P202"],
    "Velachery": ["P301", "P302"],
    "Tambaram": ["P401", "P402"]
}

def generate():
    area = random.choice(list(pipes.keys()))
    pipe = random.choice(pipes[area])

    pressure = random.uniform(30, 50)
    flow = random.uniform(10, 25)
    temp = random.uniform(25, 40)

    anomaly = random.random()

    if anomaly < 0.15:
        pressure -= random.uniform(8, 15)
        flow += random.uniform(10, 20)

    if anomaly < 0.05:
        pressure -= random.uniform(20, 30)
        flow += random.uniform(30, 50)

    return {
        "pipe_id": pipe,
        "area": area,
        "pressure": round(pressure, 2),
        "flow_rate": round(flow, 2),
        "temperature": round(temp, 2),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    supabase.table("pipe_sensor_data").insert(generate()).execute()
    print("Inserted sensor data")
    time.sleep(5)
