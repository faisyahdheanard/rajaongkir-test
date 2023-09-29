import json

import requests
from assertpy import assert_that
import pytest

from setting.endpoint import API_PROVINCE
from setting.general import api_key, max_latency
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_province import *


def test():
    # HIT API
    head = {
        "key": api_key
    }
    req = requests.get("https://api.rajaongkir.com/starter/provincesssss", headers=head)

    # VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds

    # ASSERT
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)
