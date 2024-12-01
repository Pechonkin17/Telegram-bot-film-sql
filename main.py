import logging
import asyncio
import sys

from app import main
from app.data import create_db, drop_db

if __name__ == "__main__":
    create_db()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

