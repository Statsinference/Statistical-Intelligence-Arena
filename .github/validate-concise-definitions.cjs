const fs = require('fs');
const katex = require('katex');
const path = 'dgp-submissions/tools/dgp_registry/definition_overrides.json';
const entries = JSON.parse(fs.readFileSync(path, 'utf8')).records;
let count = 0;
let errors = [];
for (const [id, record] of Object.entries(entries)) {
  for (const [scenario, target] of Object.entries(record.scenarios || {})) {
    for (const key of ['display_math', 'display_note_math']) {
      if (!target[key]) continue;
      try { katex.renderToString(target[key], {throwOnError: true, strict: 'error'}); count++; }
      catch (error) { errors.push(`${id} ${scenario} ${key}: ${error.message}`); }
    }
  }
}
console.log(`Validated ${count} math expressions, errors: ${errors.length}`);
if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
