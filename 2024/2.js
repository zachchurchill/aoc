// Day 01
// https://adventofcode.com/2024/day/2
"use strict";

import fs from "node:fs";

const data = fs.readFileSync("./inputs/2.txt", "utf8").trim();
const reports = data
  .split("\r\n")
  .map(line => line.split(/\s/))
  .map(report => report.map(level => parseInt(level)));

// Part 1
let safeReports = 0;
for (const report of reports) {
  const diffs = [];
  for (let i = 1; i < report.length; i++) {
    diffs.push(report[i] - report[i-1]);
  }
  const allIncreasing = diffs.every(el => el > 0);
  const allDecreasing = diffs.every(el => el < 0);
  const withinAcceptableRange = diffs.every(el => [1, 2, 3].includes(Math.abs(el)));
  if ((allIncreasing || allDecreasing) && withinAcceptableRange) {
    safeReports += 1;
  }
}
console.log(`Part 1 answer: ${safeReports}`);
