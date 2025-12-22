import pytest
import sqlite3


@pytest.fixture(scope="module")
def test_database():
    """创建测试数据库连接"""
    conn = sqlite3.connect(":memory:")
    # 初始化测试数据
    conn.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO user (name) VALUES ('小非'), ('小白')")
    conn.commit()
    yield conn
    conn.close()


def test_user_count(test_database):
    """集成测试：验证数据库查询"""
    cursor = test_database.cursor()
    cursor.execute("SELECT COUNT(*) FROM user")
    count = cursor.fetchone()[0]
    assert count == 2
