# vizney-styles

Add a [Vizney Styles](https://styles.vizney.com) dashboard style to your project: a `DASHBOARD.md` spec that coding agents, Tableau and Power BI can follow, and the `dashboard-style` agent skill that builds, restyles and reviews dashboards to it.

```bash
npx vizney-styles@latest add anthropic
```

Run it in your project folder. It writes:

```
DASHBOARD.md                              the spec: tokens, rules, checks
.claude/skills/dashboard-style/
  SKILL.md                                the agent skill: build, restyle, review
  tokens.css  tokens.json                 the tokens for web dashboards and scripts
  anthropic.tps                           Tableau color palettes
  powerbi-theme.json                      Power BI theme
  prompt.md                               tested prompts and Tableau / Power BI notes
```

Nothing else is touched. Then ask your agent for a dashboard; agents that read skills load `dashboard-style` by themselves, and any agent can be told to follow `DASHBOARD.md`.

```bash
npx vizney-styles@latest list                     # the styles in the catalog
npx vizney-styles@latest add anthropic --force    # replace an earlier install
npx vizney-styles@latest add anthropic --dir app  # another folder
```

The same files come from `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- anthropic` or as a zip on each style's page. Needs Node 18 or later.

Each style is a reference read from a company's public website; it is not an official design of that company, and trademarks belong to their owners. Your own company's style, made privately: https://www.vizney.com/contact-us/
