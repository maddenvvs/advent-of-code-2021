#!/bin/sh

for day in $(seq -w 1 25)
do
    aoc2021 $day "./input/day-$day.input"
done