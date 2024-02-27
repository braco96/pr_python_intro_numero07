import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("nums,esperado", [
    ([1,2,3,4], [4,16]),
    ([0, -2, 5], [0, 4]),
    ([], []),
])
def test_cuadrados_pares(nums, esperado):
    assert mod.cuadrados_pares(nums) == esperado
