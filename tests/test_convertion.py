# coding=utf-8

import json

import frictionless_ckan_mapper.ckan_to_frictionless as ctf_converter
import frictionless_ckan_mapper.frictionless_to_ckan as ftc_converter

def test_round_trip_convertion(self):
    inpath = 'tests/fixtures/full_ckan_package.json'
    indict = json.load(open(inpath))
    conv1 = ctf_converter.dataset(indict)
    conv2 = ftc_converter.package(conv1)
    assert indict == conv2
