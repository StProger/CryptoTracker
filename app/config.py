from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from dotenv import load_dotenv

import os

load_dotenv()


class Settings(BaseSettings):

    CMP_TOKEN: str = os.getenv("CMP_TOKEN")

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
