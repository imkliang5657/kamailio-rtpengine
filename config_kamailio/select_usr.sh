#!/bin/bash
NAME=$1
COL=$2
mysql kamailio -N -e  "SELECT $COL FROM subscriber Where username='$NAME';"
