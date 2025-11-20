from typing import Tuple, Type

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class S3Secret(BaseModel):
    region: str
    access_key_id: str
    secret_access_key: str
    bucket_name: str

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        yaml_file="secret.yaml", extra="ignore", case_sensitive=False
    )
    s3: S3Secret

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (YamlConfigSettingsSource(settings_cls),)


# yaml_settings = YamlSettings()
# print(yaml_settings.model_dump())
