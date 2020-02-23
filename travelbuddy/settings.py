import os

import environ

__all__ = ("get_config",)


@environ.config(prefix=None)
class _Config:

    secret_key = environ.var()

    @environ.config
    class DB:
        name: str = environ.var()
        host: str = environ.var()
        port: str = environ.var()
        user: str = environ.var()
        password = environ.var()

    database: DB = environ.group(DB)


def get_config() -> _Config:
    return environ.to_config(_Config)
