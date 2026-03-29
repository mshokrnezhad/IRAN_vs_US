# Daily War News Collection Instruction

## Purpose

Use this instruction whenever the user gives a specific date and asks for a one-day collection of developments related to the ongoing Iran-U.S.-Israel war or crisis environment.

The goal is to produce a reliable, source-driven daily brief that captures:

- official statements
- military actions and claimed actions
- diplomatic activity
- sanctions and legal measures
- casualties and damage claims
- market and infrastructure effects when relevant
- important social-media posts from official or clearly attributable accounts

This instruction is for collection and synthesis, not for advocacy or prediction.

## Scope for Each Requested Day

For the requested date, collect and summarize only developments that are:

- reported on that date, or
- officially announced on that date, or
- clearly attributable to events that occurred on that date in the main theater of conflict

If an event spans several days, include only the portion that is newly reported, newly confirmed, or newly announced on the target date.

## Source Priority

Prefer sources in this order:

1. Official government or military statements
2. Official spokesperson briefings
3. Official social-media accounts of governments, militaries, ministries, leaders, and verified institutions
4. Major wire services and reputable news agencies
5. Major international organizations when relevant

Examples of high-priority source types:

- White House, State Department, Pentagon, CENTCOM, U.S. Treasury
- Israeli Prime Minister's Office, IDF, Israeli Foreign Ministry, Israeli Defense Ministry
- Iranian Foreign Ministry, IRGC statements when clearly attributable, Iranian state outlets only when explicitly identified as state claims
- UN, IAEA, EU, Omani or Qatari mediators when relevant
- Reuters, AP, AFP, BBC, Financial Times, Wall Street Journal, New York Times
- official X/Twitter, Telegram, or website statements from the above institutions

## Social Media Rules

Only include social-media content if at least one of these is true:

- it comes from an official government, military, or institutional account
- it comes from a clearly identified senior official speaking in an official capacity
- it is directly reported and quoted by a high-confidence news source

Do not treat anonymous posts, open-source rumor accounts, or unattributed viral claims as confirmed facts.

When using social posts, record:

- platform
- account name
- official role of the speaker
- exact claim or statement
- whether it is a claim, threat, denial, confirmation, or policy signal

## What Must Be Collected

For each day, look for the following categories.

### 1. Official Statements

Collect:

- who spoke
- official title
- country or institution
- exact statement or the closest accurate summary
- main theme
- whether it was a threat, denial, confirmation, justification, warning, condolence, policy announcement, or negotiating signal

### 2. Military and Security Developments

Collect:

- strikes, interceptions, launches, air raids, naval incidents, cyber incidents, sabotage claims
- who claimed responsibility
- who was blamed
- what independent reporting could verify
- location
- time reference
- immediate consequence

### 3. Diplomatic Activity

Collect:

- negotiations
- mediation attempts
- calls between officials
- embassy or UN activity
- ceasefire or de-escalation signals
- warnings from third-party states

### 4. Sanctions, Legal, and Economic Measures

Collect:

- new sanctions
- new designations
- export controls
- asset freezes
- oil, shipping, or financial restrictions
- international legal measures
- emergency economic actions

### 5. Casualties and Damage

Collect carefully:

- killed
- wounded
- infrastructure damaged
- military assets damaged
- civilian impact

Always separate:

- confirmed figures
- claimed figures
- disputed figures

### 6. Information Environment

Collect:

- major propaganda themes
- disinformation warnings from reliable institutions
- narrative battles between the parties
- notable contradiction between official claims and independent reporting

### 7. Market and Strategic Effects

Collect only when clearly relevant:

- oil price spikes
- shipping disruptions
- airspace closures
- cyber disruptions
- regional force movements
- alerts from international watchdogs

## Verification Rules

- Distinguish clearly between `confirmed`, `claimed`, `alleged`, `denied`, and `unverified`.
- If only one side claims something, label it explicitly as that side's claim.
- If a wire service confirms partial facts but not responsibility, state that precisely.
- Do not collapse separate events into one.
- If casualty numbers differ across sources, keep the range and attribute each number.
- If a statement is important but inflammatory, quote it carefully and attribute it exactly.

## Required Output Format

When the user gives a date, produce the output in the following Markdown format.

```md
# Daily War News Brief - YYYY-MM-DD

## Scope
- Date covered: YYYY-MM-DD
- Timezone standard used: [state the standard you used, e.g. UTC or local reporting time]
- Focus: Iran / U.S. / Israel conflict and directly connected regional developments

## Executive Summary
- 3-7 bullets summarizing the most important developments of the day

## Key Events Timeline
| Time | Event | Actors | Confidence |
|------|-------|--------|------------|
| HH:MM or Unknown | Short factual description | Main actors | Confirmed / Claimed / Mixed |

## Official Statements
| Actor | Role | Country / Institution | Type | Statement Summary | Source |
|------|------|------------------------|------|-------------------|--------|
| Name | Official title | Country or institution | Threat / Denial / Confirmation / Warning / Negotiation / Policy | 1-3 sentence summary | Link |

## Military and Security Developments
| Event | Location | What Happened | Claimed By | Independently Verified? | Source |
|------|----------|---------------|-----------|--------------------------|--------|
| Short title | Place | 1-3 sentence summary | Actor or Unknown | Yes / No / Partial | Link |

## Diplomatic and Political Developments
| Event | Actors | Summary | Significance | Source |
|------|--------|---------|-------------|--------|

## Sanctions, Legal, and Economic Measures
| Measure | Issuer | Target | Summary | Source |
|--------|--------|--------|---------|--------|

## Casualties and Damage
| Category | Figure | Attribution | Confidence | Notes | Source |
|----------|--------|-------------|------------|-------|--------|

## Official Social Media and Direct Posts
| Platform | Account | Official Identity | Main Claim or Quote | Assessment | Source |
|----------|---------|-------------------|---------------------|-----------|--------|

## Information Gaps and Disputed Claims
- Bullet each major unresolved point
- State what is claimed, by whom, and what remains unverified

## Analytical Notes
- What changed compared with the previous day
- Whether escalation increased, decreased, or remained stable
- Whether the main signal was military, diplomatic, economic, or informational

## Source Log
- [Source name](URL) - why it was used
- [Source name](URL) - why it was used
```

## Style Rules for the Final Daily Brief

- Be concise, factual, and attribution-heavy.
- Prefer short sentences over dramatic language.
- Do not present propaganda as fact.
- Use direct quotes only when the wording itself matters.
- If a fact is uncertain, say so plainly.
- Separate event reporting from analysis.

## Optional Additions When Useful

If the day is especially important, add:

- `## Escalation Assessment`
- `## Comparison With Previous 72 Hours`
- `## Indicators To Watch Next`

Use these only when they add value.

## Trigger Format for Use

When the user wants a collection for a specific day, the request should be interpreted as:

`Collect the war news for YYYY-MM-DD using daily_war_news_collection_instruction.md`

Then:

1. Search official statements first
2. Search reputable wire services second
3. Cross-check claims
4. Produce the final Markdown output using the required format above

## Minimum Quality Standard

Do not finalize the daily brief unless it contains:

- at least 3 high-confidence sources unless the day is genuinely quiet
- at least one official source if any official statement exists that day
- explicit labeling of disputed claims
- a source log
- a short analytical summary of the day's meaning
