import psycopg2
import asyncio
import json

from utils import generate_token, api_push
import settings

# Connection to DB
conn = psycopg2.connect(host=settings.POSTGRE_HOST, dbname=settings.POSTGRE_DATABASE, user=settings.POSTGRE_USERNAME, password=settings.POSTGRE_PASSWORD)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Create asyncio Queue
q = asyncio.Queue()

# Connection cursor
cursor = conn.cursor()
cursor.execute("LISTEN notifications;")

# Create api token
token = generate_token(settings.API_KEY, settings.JWT_SECRET)


def listen_callback():
    conn.poll()
    q.put_nowait(conn.notifies.pop(0))


async def do_whatever():
    while True:
        data = await q.get()
        # None is the quit signal
        if data is None:
            break
        else:
            data_json = json.loads(data.payload)
            api_push(url=settings.API_PUSH_URL, token=token, message=data_json)


loop = asyncio.get_event_loop()
loop.add_reader(conn, listen_callback)
loop.run_until_complete(do_whatever())
