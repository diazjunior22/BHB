const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

// Find all matches for "translations"
const regex = /translations/g;
let count = 0;
while (regex.exec(html) !== null) {
  count++;
}
console.log('Occurrences of word "translations":', count);

// Find where translations is assigned or modified
const lines = html.split('\n');
lines.forEach((line, index) => {
  if (line.includes('translations')) {
    console.log(`${index + 1}: ${line.trim()}`);
  }
});
