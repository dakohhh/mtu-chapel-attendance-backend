from ..settings import settings
from mongoengine import connect, disconnect


async def connect_to_mongo():

    try:
        connect(
            host=settings.MONGODB_URI,
            name="MTU_CHAPEL",
            tls=True if not settings.DEBUG else False,
            tlsCAFile=settings.APPLICATION_CERTIFICATE if not settings.DEBUG else None,
        )

        print(':::> Connection to MongoDB established.')
    except Exception as e:
        print(f"<::: Error connecting to MongoDB: {e}")



async def disconnect_from_mongo():
    disconnect()
    print('Connection to MongoDB closed.')
