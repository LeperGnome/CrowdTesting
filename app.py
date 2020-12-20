from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager
from peewee import PostgresqlDatabase
import os


class AppContext:
    project_root = os.path.dirname(os.path.abspath(__file__))
    _flaskapp = None
    _instance = None
    _env = None
    _jwt = None
    _db = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = AppContext()

        return cls._instance

    @property
    def flaskapp(self) -> Flask:
        if self._flaskapp is None:
            self._flaskapp = Flask('CrowdTesting')
        return self._flaskapp

    @property
    def jwt(self) -> JWTManager:
        if self._jwt is None:
            self._jwt = JWTManager(self.flaskapp)
        return self._jwt

    @property
    def env(self) -> Env:
        if self._env is None:
            env = Env()
            env_path = os.path.join(self.project_root, '.env')
            env.read_env(env_path)

            self._env = env

        return self._env

    @property
    def db(self) -> PostgresqlDatabase:
        if self._db is None:
            env = self.env
            self._db = PostgresqlDatabase(
                database=env('DB_SCHEMA'),
                user=env('DB_USER'),
                password=env('DB_PASSWORD'),
                host=env('DB_HOST'),
                port=env('DB_PORT'),
            )
        return self._db
