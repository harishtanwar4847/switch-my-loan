import os

def boot_session(bootinfo):
    bootinfo.sml_encryption_key = os.getenv("SML_ENCRYPTION_KEY") or "AAAAAAAAZZZZZZZZ"
    bootinfo.sml_nucleus_base_url = os.getenv("SML_NUCLEUS_BASE_URL") or "http://localhost:3000"
