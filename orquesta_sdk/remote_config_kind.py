from enum import Enum


class OrquestaRemoteConfigKind(Enum):
    Boolean = "boolean"
    Integer = "integer"
    String = "string"
    List = "list"
    Json = "json"
