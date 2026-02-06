from supabase import create_client

supabase = create_client(
    "https://dstilpwjehgsfgbuakjf.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRzdGlscHdqZWhnc2ZnYnVha2pmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2ODc1NTA2NywiZXhwIjoyMDg0MzMxMDY3fQ.SNwYXUXV4GwFZFYAS4seKMaIXxKWcHlZMJabUTGKsc0"
)

print("✅ Supabase connected successfully")
