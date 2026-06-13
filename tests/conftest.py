# Tests live in tests/ but import modules from the repo root (serve, tile_harness,
# dashboard_fixture). Put the repo root on sys.path so those imports resolve.
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
