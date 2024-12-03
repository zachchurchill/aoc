// Day 02
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

// Part 2
safeReports = 0;
function isReportSafe(report) {
  const diffs = [];
  for (let i = 1; i < report.length; i++) {
    diffs.push(report[i] - report[i-1]);
  }
  const allIncreasing = diffs.every(el => el > 0);
  const allDecreasing = diffs.every(el => el < 0);
  const withinAcceptableRange = diffs.every(rule2);
  return (allIncreasing || allDecreasing) && withinAcceptableRange;
}
// Not proud of this but it worked
for (const report of reports) {
  if (isReportSafe(report)) {
    safeReports += 1;
  } else {
    for (let i = 0; i < report.length; i++) {
      if (isReportSafe([...report.slice(0, i), ...report.slice(i+1, report.length)])) {
        safeReports += 1;
        break;
      }
    }
  }
}
console.log(`Part 2 answer: ${safeReports}`);
