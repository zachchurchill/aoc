// Day 03
// https://adventofcode.com/2024/day/3
"use strict";

import fs from "node:fs";

const data = fs.readFileSync("./inputs/3.txt", "utf8").trim();

// Part 1
const mulMatches = Array.from(data.matchAll(/mul\((\d+),(\d+)\)/g));
const total = mulMatches
  .map(match => parseInt(match[1]) * parseInt(match[2]))
  .reduce((a, b) => a + b, 0);
console.log(`Part 1 answer: ${total}`);

// Part 2
const matches = Array.from(data.matchAll(/mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)/g));
let enabled = true;
let newTotal = 0;
for (const match of matches) {
  if (match[0] === "don't()") {
    enabled = false;
    continue;
  } else if (match[0] === "do()") {
    enabled = true;
    continue;
  }

  if (enabled) {
    newTotal += parseInt(match[1]) * parseInt(match[2]);
  }
}
console.log(`Part 2 answer: ${newTotal}`);
