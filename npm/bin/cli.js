#!/usr/bin/env node
// vizney-styles: put a Vizney Styles dashboard style in the current project.
//
//   npx vizney-styles@latest add anthropic
//
// Writes DASHBOARD.md (the spec) to the project root and the dashboard-style agent skill to
// .claude/skills/dashboard-style/ (SKILL.md with tokens.css, tokens.json, <style>.tps,
// powerbi-theme.json and prompt.md). The same files as install.sh and the zip on each style's page.
'use strict';

const fs = require('fs');
const path = require('path');

const BASE = (process.env.VIZNEY_STYLES_BASE || 'https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main').replace(/\/$/, '');
const SITE = 'https://styles.vizney.com';
const SKILL_DIR = path.join('.claude', 'skills', 'dashboard-style');
const VERSION = require('../package.json').version;

const HELP = `vizney-styles ${VERSION} — dashboard styles that coding agents, Tableau and Power BI can follow

Usage
  npx vizney-styles@latest add <style>     add a style to the project in this folder
  npx vizney-styles@latest list            list the styles in the catalog

Options
  --dir <path>   the project folder (default: the current folder)
  --force        replace DASHBOARD.md and the skill if they are already there
  -h, --help     this help
  -v, --version  the version

What "add" writes
  DASHBOARD.md                              the spec: tokens, rules, checks
  .claude/skills/dashboard-style/SKILL.md   the agent skill: build, restyle, review
  .claude/skills/dashboard-style/           tokens.css, tokens.json, <style>.tps, powerbi-theme.json, prompt.md

Styles and live samples: ${SITE}`;

function fail(msg, code = 1) {
  process.stderr.write(msg.replace(/\n?$/, '\n'));
  process.exit(code);
}

async function get(url, as = 'text') {
  let res;
  try {
    res = await fetch(url, { headers: { 'user-agent': `vizney-styles/${VERSION}` } });
  } catch (e) {
    fail(`Could not reach ${new URL(url).host}: ${e.cause ? e.cause.code || e.cause.message : e.message}`);
  }
  if (!res.ok) return null;
  return as === 'json' ? res.json() : Buffer.from(await res.arrayBuffer());
}

async function list() {
  const cat = await get(`${BASE}/catalog.json`, 'json');
  if (!cat) fail('Could not read the catalog. See ' + SITE);
  for (const s of cat.styles) {
    process.stdout.write(`${String(s.number).padStart(2, '0')}  ${s.slug.padEnd(16)} ${s.name} — ${s.words}\n    ${s.sample}\n`);
  }
  process.stdout.write(`\nAdd one: npx vizney-styles@latest add <style>\n`);
}

async function add(style, dir, force) {
  if (!style) fail('Which style? For example: npx vizney-styles@latest add anthropic\nSee them all: npx vizney-styles@latest list');
  if (!/^[a-z0-9-]+$/.test(style)) fail(`Unknown style: ${style}`);
  const root = path.resolve(dir);
  if (!fs.existsSync(root) || !fs.statSync(root).isDirectory()) fail(`Not a folder: ${root}`);
  const spec = path.join(root, 'DASHBOARD.md'), skill = path.join(root, SKILL_DIR);
  if (!force && (fs.existsSync(spec) || fs.existsSync(path.join(skill, 'SKILL.md')))) {
    fail(`DASHBOARD.md or ${SKILL_DIR} already exists in ${root}.\nRun again with --force to replace them: npx vizney-styles@latest add ${style} --force`);
  }
  // Download everything first, so a failed download leaves the project untouched
  const files = [['DASHBOARD.md', spec], ['skill/SKILL.md', path.join(skill, 'SKILL.md')]]
    .concat(['tokens.css', 'tokens.json', `${style}.tps`, 'powerbi-theme.json', 'prompt.md'].map(f => [f, path.join(skill, f)]));
  const got = [];
  for (const [src, dest] of files) {
    const body = await get(`${BASE}/${style}/${src}`);
    if (!body) fail(`No style called "${style}". See the catalog: npx vizney-styles@latest list`);
    got.push([dest, body]);
  }
  fs.mkdirSync(skill, { recursive: true });
  for (const [dest, body] of got) fs.writeFileSync(dest, body);
  const rel = p => path.relative(process.cwd(), p) || '.';
  process.stdout.write(`Added the ${style} dashboard style to ${rel(root)}:
  DASHBOARD.md                      the spec
  ${SKILL_DIR}/   the skill (build, restyle, review) and the tool files

Next
  Ask your agent: "Build our monthly operations dashboard to DASHBOARD.md."
  Tableau: paste the palettes in ${path.join(SKILL_DIR, style + '.tps')} into My Tableau Repository/Preferences.tps.
  Power BI: View > Themes > Browse for themes > ${path.join(SKILL_DIR, 'powerbi-theme.json')}.
  Live sample: ${SITE}/${style}/
`);
}

async function main() {
  const args = process.argv.slice(2);
  const flags = new Set(args.filter(a => a.startsWith('-')));
  const di = args.indexOf('--dir');
  const dir = di >= 0 ? args[di + 1] : '.';
  if (di >= 0 && (!dir || dir.startsWith('-'))) fail('--dir needs a folder');
  const pos = args.filter((a, i) => !a.startsWith('-') && !(di >= 0 && i === di + 1));
  if (flags.has('-v') || flags.has('--version')) return process.stdout.write(VERSION + '\n');
  if (flags.has('-h') || flags.has('--help') || pos.length === 0) return process.stdout.write(HELP + '\n');
  const unknown = [...flags].filter(f => !['--force', '--dir'].includes(f));
  if (unknown.length) fail(`Unknown option: ${unknown[0]}\n\n${HELP}`);
  const [cmd, style] = pos;
  if (cmd === 'add') return add(style, dir, flags.has('--force'));
  if (cmd === 'list') return list();
  fail(`Unknown command: ${cmd}\n\n${HELP}`);
}

main().catch(e => fail(e.stack || String(e)));
