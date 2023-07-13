# Александра Чернякова, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_requests
import data
import configuration
import requests
import pytest

def get_order_track():
    response = sender_stand_requests.post_new_order(data.order_body)
    return response.json()["track"]

def get_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER + str(track))
    return response.json()

def positive_assert(track):
    response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER + str(track))
    assert response.status_code == 200

def test_create_order_success_response():
    positive_assert(get_order_track())
