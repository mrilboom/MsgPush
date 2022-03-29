#!/bin/bash
pid=`ps -ef | grep WatchTemp |head -n 1 | awk '{print$2}'`
kill $pid