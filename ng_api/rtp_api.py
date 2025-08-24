#!/usr/bin/env python3

import aiohttp
import asyncio
import bencodepy
import random

async def main():
    headers = {'content-type': 'application/x-rtpengine-ng'}
    async with aiohttp.ClientSession(headers=headers) as session:
        cookie = f"0_{random.randint(1000, 9999)}_1"
        bdata = bencodepy.encode({'command': 'list'}).decode('utf-8')
        data = f"{cookie} {bdata}"
        async with session.post('http://163.22.22.62:2225/ng', data=data) as response:
            result = await response.text()
            result = result.split(" ", 1)
            r = bencodepy.decode(result[1])
            print(r)

asyncio.run(main())
