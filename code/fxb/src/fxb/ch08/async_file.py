import os
import asyncio
import aiofiles


async def write_file(filename: str, content: str):
    """异步写入文件"""
    async with aiofiles.open(filename, "w") as f:
        await f.write(content)
    print(f"已写入文件: {filename}")


async def read_file(filename: str):
    """异步读取文件"""
    async with aiofiles.open(filename, "r") as f:
        content = await f.read()
    print(f"从 {filename} 读取到 {len(content)} 字符")
    return content


async def main():
    # 并发执行文件操作
    await asyncio.gather(
        write_file("test1.txt", "Hello, AsyncIO!\n"),
        write_file("test2.txt", "Another file.\n"),
    )

    # 并发读取文件
    c1, c2 = await asyncio.gather(
        read_file("test1.txt"),
        read_file("test2.txt"),
    )
    assert c1 == "Hello, AsyncIO!\n"  # 验证内容,预期断言成功
    assert c2 == "Another file.\n"  # 验证内容,预期断言成功

    # 清理临时文件
    os.remove("test1.txt")
    os.remove("test2.txt")


if __name__ == "__main__":
    asyncio.run(main())
