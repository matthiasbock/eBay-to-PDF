#!/bin/bash

set MOZ_NO_REMOTE=1
firefox -no-remote -print http://www.ebay.de/ -printmode pdf -printfile ./ebay.pdf
