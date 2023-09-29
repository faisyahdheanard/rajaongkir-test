import json

import requests
from assertpy import assert_that
import pytest

from setting.endpoint import API_COST
from setting.general import api_key, max_latency
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_cost import *


def test():
    # HIT API
    head = {
        "key": api_key
    }
    payload = {
        "origin" : "1",
        "destination" : "60",
        "weight" : 1000,
        "courier" : "pos"
    }
    req = requests.post(API_COST, headers=head, json=payload)
    # print(req.json())

    # VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    results = req.json().get("rajaongkir")["results"]


    # ASSERT
    assert_that(status_code).is_equal_to(200)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("OK")
    assert_that(results).is_type_of(list)
    assert_that(results).is_not_none()
    validate_json_schema(instance=req.json(), schema=schema_list_cost_normal)


