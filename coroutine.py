import asyncio
import time
import random
@asyncio.coroutine
def ping_server(ip):  # async key word introduced in python 3.5
    print("ping_server")
    yield from asyncio.sleep(random.randint(0, 5))

  #decorator works same as async
async def load_file(i):
    s = random.randint(0,5)
    print(f"thread {i}, start sleep {s}")
    await asyncio.sleep(s)  
    print(f"thread {i}, sleep {s} finish")

def call_back_obj(i):
    print(f"callback: thread {i} finish")

async def coroutine_obj(total):
    print(f"started coroutine_obj at {time.strftime('%X')}")
    for i in range(total):
        await load_file(i)
    print(f"started coroutine_obj at {time.strftime('%X')}")

async def task_obj(total,loop):
    tasks=[]
    for i in range(total):
        #tasks.append(asyncio.create_task(load_file(i)))    asyncio.create_task introduce in 3.7
        task = loop.create_task(load_file(i))
        tasks.append(task)
        #task.add_done_callback(call_back_obj(i))
    print(f"started task_obj at {time.strftime('%X')}")
    for t in tasks:
        await t
    print(f"started task_obj at {time.strftime('%X')}")

total=5
loop = asyncio.get_event_loop()
loop.run_until_complete(task_obj(5, loop))
#loop.run_until_complete(coroutine_obj(total))
#asyncio.run(coroutine_obj(total))  asyncio.run introduce in 3.7