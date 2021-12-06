#!/bin/sh

DECEMBER_FIRST=$(date -j '113000002021' +%s)
TODAY=$(date +%s)
DAYS_PAST=$((($TODAY - $DECEMBER_FIRST)/(3600*24)))
if (($DAYS_PAST > 25)); then
    $DAYS_PAST=25
fi

for day in $(seq -f "%02g" -w 1 $DAYS_PAST)
do
    aoc2021 $day "./input/day-$day.input"
done