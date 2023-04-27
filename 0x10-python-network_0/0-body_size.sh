#!/bin/bash
#  a script that takes and sends a request to that URL, displays the size
curl -s "$1" |  wc -c
