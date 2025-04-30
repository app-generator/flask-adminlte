# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, re, uuid
from colorama import Fore, Style
from apps.authentication.models import Users
from apps.config import Config
from marshmallow import ValidationError
from apps.messages import Messages
from functools import wraps
from flask import request
from uuid import uuid4
import datetime, time
message = Messages.message

Currency = Config.CURRENCY
PAYMENT_TYPE = Config.PAYMENT_TYPE
STATE = Config.STATE


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def get_ts():
    return int(time.time())

def password_validate(password):
    """ password validate """
    msg = ''
    while True:
        if len(password) < 6:
           msg = "Make sure your password is at lest 6 letters"
           return msg
        elif re.search('[0-9]',password) is None:
            msg = "Make sure your password has a number in it"
            return msg
        elif re.search('[A-Z]',password) is None: 
            msg = "Make sure your password has a capital letter in it"
            return msg
        else:
            msg = True
            break
        
    return True

def emailValidate(email):
    """ validate email  """
    if re.fullmatch(regex, email):
        return True
    else:
        return False

# santise file name
def sanitise_fille_name(value):
    """ remove special char  """
    return value.strip().lower().replace(' ', '_').replace('(', '').replace(')', '').replace(',', '').replace('=','_').replace('-', '_').replace('#', '')

def createFolder(folder_name):
    """ create folder for save csv """
    if not os.path.exists(f'{folder_name}'):
        os.makedirs(f'{folder_name}')

    return folder_name


def uniqueFileName(file_name):
    """ for Unique file name"""
    file_uuid = uuid.uuid4()
    IMAGE_NAME = f'{file_uuid}-{file_name}'
    return IMAGE_NAME

def serverImageUrl(file_name):
    """ for Unique file name"""
    url = f'{FTP_IMAGE_URL}{file_name}'
    return url

def errorColor(error):
    """ for terminal input error color """
    print(Fore.RED + f'{error}')
    print(Style.RESET_ALL)
    return True

def splitUrlGetFilename(url):
    """ image url split and get file name  """
    return url.split('/')[-1]

def validateCurrency(currency):
    """ check currency  """
    # if check currency validate or not
    if currency not in list(Currency.keys()):
        raise ValidationError(
            f"{message['invalid_currency']}, expected {','.join(Currency.keys())}", 422)

def validatePaymentMethod(payment):
    """ check valid payment methods  """
    # if check PAYMENT_TYPE validate or not
    if payment not in list(PAYMENT_TYPE.keys()):
        raise ValidationError(
            f"{message['invalid_payment_method']}, expected {expectedValue(PAYMENT_TYPE)}", 422)
        
    else:
        value = 0
        if payment == "cc":
            value =  1
        elif payment == "paypal":
            value = 2
        else:
            value = 3

    return value 

def validateState(state):
    """ check valid state methods  """
    # if check state  validate or not
    if state not in list(STATE.keys()):
        raise ValidationError(
            f"{message['invalid_state']}, expected {expectedValue(STATE)}", 422)
        
    else:
        value = 0
        if state == "completed":
            value =  1
        elif state == "pending":
            value = 2
        else:
            value = 3

    return value 

 
def expectedValue(data):
    """ key get values """
    values = []
    for k,v in data.items():
        values.append(f'{v}.({k})')

    return ",".join(values)


def createAccessToken():
    """ create access token w"""
    rand_token = uuid4()

    return f"{str(rand_token)}"


# token validate
def token_required(f):
    """ check token """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "error": "Unauthorized"
            }, 401
        try:
            current_user = Users.find_by_api_token(token)
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "error": "Unauthorized"
            }, 401
            # if not current_user["active"]:
            #     abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "error": str(e)
            }, 500

        return f(current_user, **kwargs)

    return decorated
