from __future__ import annotations
from typing import Pattern, Tuple, List
from pydantic import BaseModel, Field
from enum import Enum


class EntityDefaults(BaseModel):
    Model: str
    Version: str | None = None
    Node: str | None = None


class PackageC(BaseModel):
    Name: str
    Version: str | None = None


class Defaults(BaseModel):
    Inputs: EntityDefaults | None = None
    Outputs: EntityDefaults | None = None
    Package: PackageC | None = None



class FromToList(BaseModel):
    items: Tuple[str, str]


class NPSpec(BaseModel):
    Node: str
    Prop: str


class NPIdentitySpec(BaseModel):
    From: NPSpec
    To: NPSpec


class IOSpec(BaseModel):
    Model: str
    Version: str
    Node: str
    Props: List[str]


class IdentitySpec(BaseModel):
    From: IOSpec
    To: IOSpec


class TfStepSpec(BaseModel):
    Package: PackageC
    Params: list | dict | None = None
    Entrypoint: str
    

class GeneralTransform(BaseModel):
    Inputs: List[IOSpec]
    Outputs: List[IOSpec]
    Steps: List[TfStepSpec]


class IdentityTransform(GeneralTransform):
    Steps: List[TfStepSpec] = Field(
        default_factory=lambda: [TfStepSpec(Package={"Name":"Identity"},
                                            Entrypoint="identity")]
        )
    
