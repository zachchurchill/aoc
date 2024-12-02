// Day 01
// https://adventofcode.com/2024/day/1
"use strict";

import fs from "node:fs";

const data = fs.readFileSync("./inputs/1.txt", "utf8").trim();
const locationIds = data.split("\n").map(line => line.split(/\s+/));

const leftLocationIds = [];
const rightLocationIds = [];
for (const [ left, right ] of locationIds) {
  leftLocationIds.push(parseInt(left));
  rightLocationIds.push(parseInt(right));
}
leftLocationIds.sort();
rightLocationIds.sort();

const totalDistance = leftLocationIds
  .map((locationId, idx) => Math.abs(locationId - rightLocationIds[idx]))
  .reduce((x, y) => x + y);

console.log(`Part 1 answer: ${totalDistance}`);

// Construct a map with the values as keys & occurences summed as values then compare/iterate
const rightIds = new Map();
for (const el of rightLocationIds) {
  rightIds.set(el, (rightIds.get(el) ?? 0) + 1);
}

let total = 0;
for (const el of leftLocationIds) {
  total += el * (rightIds.get(el) ?? 0);
}
console.log(`Part 2 answer: ${total}`);
