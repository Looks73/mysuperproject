# tests/test_try_me.py
from mysuperproject.lib import try_me

def test_try_me():
    assert try_me().startswith('Welcome')