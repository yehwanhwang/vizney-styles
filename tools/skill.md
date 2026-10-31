---
name: dashboard-style
description: Build, restyle or review dashboards, charts, KPI cards and report screens to the house style in DASHBOARD.md (__STYLE__ · __WORDS__) — colors, chart choice, number and date formats, layout, accessibility, and Tableau or Power BI settings. Use whenever a task makes or changes a dashboard or chart, or asks whether one follows the style.
---

# Dashboard style: __STYLE__

The house style for dashboards in this project is written down in `DASHBOARD.md` at the project root. It decides colors, chart forms, number formats, layout and checks, so do not invent any of them and do not ask the user about style; ask only about content (data, audience, period) when it is missing.

Files (this folder holds the style's tool files; `DASHBOARD.md` sits at the project root):

| File | Use |
|---|---|
| `DASHBOARD.md` (project root) | the spec: read it in full before any dashboard work |
| `tokens.css` | CSS custom properties for web dashboards; load it or copy its values |
| `tokens.json` | the same values as data, for scripts and other tools |
| `__SLUG__.tps` | Tableau color palettes; the user pastes them into `My Tableau Repository/Preferences.tps` |
| `powerbi-theme.json` | Power BI theme; the user imports it under View → Themes → Browse for themes |
| `prompt.md` | tested prompts and the Tableau and Power BI notes for people |

## Pick the mode

- **Build**: the user wants a new dashboard, report screen or chart.
- **Restyle**: the user has a screen (a file, a component, a screenshot, a workbook) and wants it to follow the style without changing its data.
- **Review**: the user asks whether something follows the style, or wants feedback before sharing.

If a request mixes them (for example "build it, then check it"), do them in that order.

## Build

1. Read `DASHBOARD.md` in full. Note the sections you will use: Layout Principles, Component Stylings, Charts, Data Colors, Numbers, Dates & Units.
2. Write a short plan before code: the headline (the result in one sentence), the four key figures, and every view with its question and the chart form that "Charts → Choose by the question" gives for it. Keep at most seven views per screen. Show the plan to the user when the dashboard is large or the request is vague.
3. Build with the tokens only: the colors in `tokens.css` / Data Colors, the type scale, the card anatomy (figure label → finding title → subtitle → keys → chart or table → note).
4. Write every card title as the finding and every note as the method, in the formats of Numbers, Dates & Units for each language you ship.
5. Add a hover tooltip, keyboard control and a screen-reader table to every chart.
6. Run the checks below, fix what fails, then report what passed.

## Restyle

1. Read `DASHBOARD.md`, then the screen. Keep its data, filters and logic.
2. Move every view onto the card anatomy, map colors to the tokens (the subject's color first, everyone else gray), replace chart forms that break "Charts" (pie, donut, dual axis, rainbow categories), and convert number formats.
3. List what you changed, grouped by section of `DASHBOARD.md`, then run the checks.

## Review

Read `DASHBOARD.md`, then the screen, and answer with a table: rule · what the screen does · severity (must fix / should fix / fine) · the fix. Cover every item of the checks below and anything in Do's and Don'ts. Change nothing unless the user asks you to fix it.

## Checks

Run the checklist at the end of `DASHBOARD.md` ("Agent Prompt Guide"). At the least:

- The headline states the result; key figures carry signed changes colored by whether the change is good.
- Every view sits on the same card; every title states a finding; every note explains the method.
- Only the colors in Data Colors; the subject has one color everywhere; at most three hues plus gray in a chart.
- Labels on points and line ends instead of legends where possible; side-by-side charts share a scale; no dual axis, pie or donut.
- Numbers, dates and units follow the spec in every language shipped.
- Text ≥ 4.5:1 on its surface; marks below 3:1 have a second cue.
- Every chart has a tooltip, keyboard control and a data table; nothing breaks at 390px wide.

## Tableau and Power BI

When the work is in Tableau or Power BI, give the user the settings rather than code: the palette or theme file from this folder, then the per-sheet or per-visual settings from Tool Mapping in `DASHBOARD.md` and the notes in `prompt.md`. Say which steps the user does by hand (installing palettes or themes, fonts on viewing machines).

Style source: https://styles.vizney.com/__SLUG__/ · Vizney Styles. __DISCLAIMER__
