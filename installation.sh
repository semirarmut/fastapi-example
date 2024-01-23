#!/bin/bash

set -eu -o pipefail

pip install fastapi
pip install "uvicorn[standard]"