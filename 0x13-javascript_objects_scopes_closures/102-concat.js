#!/usr/bin/node
/* a script that concats 2 files. */
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, dataA + dataB);
