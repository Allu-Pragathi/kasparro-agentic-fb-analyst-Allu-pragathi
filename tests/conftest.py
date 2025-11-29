# tests/conftest.py
# Ensure repo root is on sys.path so "from src..." imports work during pytest collection.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # parent of tests/ = repo root
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
