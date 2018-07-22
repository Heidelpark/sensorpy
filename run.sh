#!/bin/sh
export AMPY_PORT=/dev/ttyUSB0
ampy run "$1"
#ampy run -n "$1"
