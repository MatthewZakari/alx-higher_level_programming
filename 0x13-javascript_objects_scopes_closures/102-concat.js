#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;
    const concatenatedData = dataA.trim() + '\n' + dataB.trim() + '\n';
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) throw err;
    });
  });
});
