import pytest

"""
一个测试用例中有多个数据需要进行比较
一个个比较或者放到一个数据结构里面全面比较
    全面比较，无法知道那个值不对
    一个个比较数值，第一个失败就退出
"""

"""
def test_assume():
    pytest.assume(1 == 2)
    pytest.assume(2 == 2)
    pytest.assume(3 == 2)

"""


@pytest.mark.parametrize("x,y", [
    (3 + 5, 9),
    (2 + 4, 6),
    (6 * 9, 45),
    ("testerhome", "testerhome")
])
def test_add(x, y):
    assert x == y
