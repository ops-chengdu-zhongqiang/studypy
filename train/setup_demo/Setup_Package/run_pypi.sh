#!/bin/bash

source /Users/zhongqiang/.virtualenvs/courses/bin/activate
pip install pypiserver

cd /Users/study/studypy/train/setup_demo/Setup_Package/

exec pypi-server  -p 8000  --fallback-url http://pypi.doubanio.com/simple /Users/study/studypy/train/setup_demo/Setup_Package/dist/


