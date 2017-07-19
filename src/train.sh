#!/bin/bash
../common/crf++/bin/crf_learn -f 4 -p 40 -t -c 3 template crf_train.data model > crf_train.rst
#../common/crf++/bin/crf_test -m model crf_test.data > crf_test.rst
