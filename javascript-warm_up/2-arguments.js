#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
  process.exit(1);
} else if (args.length === 1) {
  console.log('Argument found');
  process.exit(1);
} else {
  console.log('Arguments found');
  process.exit(1); // quitte le script avec code d'erreur
}
