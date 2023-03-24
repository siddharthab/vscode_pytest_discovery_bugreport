import pytest

import proj.mul

def test_mul():
    assert proj.mul.op(2, 3) == 6
