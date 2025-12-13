import asyncio
import httpx


async def fetch_url(client: httpx.AsyncClient, url: str)-> tuple[str, int, int]:
    """异步获取URL内容"""
    try:
        response = await client.get(url, timeout=20.0)
        return url, response.status_code, len(response.text)
    except Exception as e:
        return url, str(e), 0


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/404",
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, status, length in results:
            print(f"{url}: 状态={status}, 长度={length}")


if __name__ == "__main__":
    asyncio.run(main())
