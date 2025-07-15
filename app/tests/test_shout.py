import pytest

import app.models.shout as shout_model

def test_shout():
    # GIVEN a text input
    given = 'hello'
    # WHEN it is transformed
    ret = shout_model.shout(given)
    # THEN it should be uppercase
    assert('HELLO' == ret)
