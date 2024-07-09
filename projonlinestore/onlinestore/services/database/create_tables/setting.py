from starlette.config import Config
from starlette.datastructures import secret

try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=secret)
TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=secret)
