from typing import List
import datetime as _dt
import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    username: str

class UserCreate(_UserBase):
    password: str

class User(_UserBase):
    id: int
    
    class Config:
        orm_mode = True




class _GraphBase(_pydantic.BaseModel):
    nome_grafo: str
    numerosDeNo: int
    numeroDeArestas: int

class GraphCreate(_GraphBase):
    user_id: int

class Graph(_GraphBase):
    id: int
    
    class Config:
        orm_mode = True



class _NodeBase(_pydantic.BaseModel):
    nome_no: str

class NodeCreate(_NodeBase):
    grafo_id: int

class Node(_NodeBase):
    id: int  
    class Config:
        orm_mode = True



class _EdgeBase(_pydantic.BaseModel):
    peso: int

class EdgeCreate(_EdgeBase):
    source_id: int
    target_id: int
    grafo_id: int

class Edge(_EdgeBase):
    id: int   
    class Config:
        orm_mode = True
