import os

def boot_session(bootinfo):
    bootinfo.sml_encryption_key = os.getenv("SML_ENCRYPTION_KEY") or "3JHSSN8XWY0SL3I3"
    bootinfo.sml_nucleus_base_url = os.getenv("SML_NUCLEUS_BASE_URL") or "https://nucleus.switchmyloan.in"
