import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power=True, Channel=0, Volume=0"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power=True, Channel=0, Volume=0"
    tv.power()
    assert str(tv) == "Power=False, Channel=0, Volume=0"

def test_mute():
    tv = Television()
    tv.power()  # Turn TV on
    tv.volume_up()  # Increase volume to 1
    tv.mute()
    assert str(tv) == "Power=True, Channel=0, Volume=0"
    tv.mute()
    assert str(tv) == "Power=True, Channel=0, Volume=1"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power=True, Channel=1, Volume=0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should wrap around to channel 0
    assert str(tv) == "Power=True, Channel=0, Volume=0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Should wrap around to channel 3
    assert str(tv) == "Power=True, Channel=3, Volume=0"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power=True, Channel=0, Volume=1"
    tv.volume_up()
    tv.volume_up()  # Should remain at volume 2
    assert str(tv) == "Power=True, Channel=0, Volume=2"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power=True, Channel=0, Volume=1"
    tv.volume_down()
