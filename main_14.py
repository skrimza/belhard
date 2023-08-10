import threading
from time import sleep

lock1 = threading.lock()

def main():
    for _ in range(10):
        with lock1:
            print(threading.current_thread().name)
        sleep(1)

if __name__ == '__main__':
    threads = [threading.Thread(target=main, name=f'Thread-{i}') for i in range(10)]
    for thread in threads:
        thread.start()

from asyncio import Lock, Semaphore, Barrier, Queue, sleep, run

async def foo():
    for _ in range(10):
        print(current_task().get_name())
        await sleep(1)

async def main():
    tasks = [create_task(foo(), name=f'Task-{i}') for i in]