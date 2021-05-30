# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:18:30 2021

@author: tomcs
"""
from typing import Optional,List,Union
from pydantic import BaseModel,AnyUrl,EmailStr,constr,conint,conlist,PositiveInt,confloat
from datetime import datetime



class Credit_card(BaseModel):
    holder_name :str
    exp_date : str
class payments(BaseModel):
    payment_type: str
    credit_card : Optional[Credit_card]
class users(BaseModel):
    member_id : int
    role:str
    name : str
    email : str
    password : str
class memberships(BaseModel):
    membership_type: str
    active : bool
    price: int
    valid: int
class invoices(BaseModel):
    membership : memberships
    member_id : int
    payment : payments
    sold : datetime
    start : datetime
    end: datetime
class invoices_list(BaseModel):
    data : List[invoices]