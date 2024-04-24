#!/usr/bin/node
const fs = require('fs');

const firstSourceFilePath = process.argv[2];
const secondSourceFilePath = process.argv[3];
const destinationFilePath = process.argv[4];

const firstSourceFileContent = fs.readFileSync(firstSourceFilePath, 'utf8');
const secondSourceFileContent = fs.readFileSync(secondSourceFilePath, 'utf8');

const concatenatedContent = firstSourceFileContent + secondSourceFileContent;

fs.writeFileSync(destinationFilePath, concatenatedContent);
