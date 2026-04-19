# ChemClaw-Lab

[![Status](https://img.shields.io/badge/status-research%20starter-blue)](#project-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docs First](https://img.shields.io/badge/repo-docs--first-orange)](#repository-map)

ChemClaw-Lab is a messaging-native, event-centric, multi-agent framework for chemistry laboratory operations.

It is designed for small academic chemistry labs where daily work is fragmented across chat apps, spreadsheets, screenshots, and informal notes. The goal is to turn those fragmented inputs into structured, traceable, and actionable lab memory for:

- inventory and consumable management
- experiment memory construction
- planning and internal instrument booking

The long-term aim is to make ChemClaw-Lab both:

1. a credible research project suitable for paper submission
2. a reusable open-source starter framework for AI-assisted lab operations

![ChemClaw-Lab concept overview](assets/chemclaw-overview.png)

*Concept illustration for ChemClaw-Lab, showing the messaging-native, multi-agent, event-centric lab operations workflow.*

## Why this project exists

Small academic labs often struggle with:

- delayed inventory updates
- fragmented experiment records
- weak visibility for PI supervision
- disconnected planning, inventory, and scheduling workflows

ChemClaw-Lab treats these as one operational systems problem instead of several isolated nuisances.

## Core idea

Instead of forcing researchers to leave WeChat, WhatsApp, or similar communication tools, ChemClaw-Lab starts from the channels they already use.

Raw messages, images, and files are first converted into **structured events**, then used to update operational state, generate summaries, or coordinate bookings.

This gives the system four defining properties:

- **messaging-native**
- **multi-agent**
- **event-centric**
- **traceable**

## What ChemClaw-Lab covers

The current project scope is intentionally narrow and realistic:

- around 10 lab members
- internal instruments only
- an existing chemical inventory table as a starting data source
- a target outcome of demo + benchmark + open-source starter repo
- an orientation toward lab operations, not a general chatbot

## System components

### Orchestrator
Routes requests, decomposes mixed tasks, and coordinates specialist agents.

### Agent A, Chemical & Consumable Manager
Handles stock lookup, location lookup, inventory updates, and restocking suggestions.

### Agent B, Experiment Memory Manager
Turns fragmented notes, photos, and screenshots into structured experiment memory and PI-facing summaries.

### Agent C, Planning & Booking Manager
Checks dependencies, drafts short-horizon plans, and coordinates internal instrument booking.

### Audit / Confirmation Layer
Prevents risky or uncertain writes from being silently applied.

## Event-first workflow

```text
raw message
  -> specialist parsing
  -> structured event
  -> audit / confirmation
  -> state update or summary / planning output
```

This design helps preserve evidence, reduce unsupported writes, and make the system benchmarkable.

## Repository map

```text
ChemClaw-Lab/
├── README.md
├── LICENSE
├── PROJECT_STATUS.md
├── PROJECT_STATUS_CN.md
├── CONTRIBUTING.md
├── DEVELOPMENT_LOG.md
├── agents/
├── assets/
├── benchmark/
├── demo_data/
├── docs/
├── scripts/
├── src/
└── tests/
```

### Key folders

- `docs/` - system overview, architecture, schema, roadmap, deployment notes, and project guidance
- `agents/` - role specifications for the orchestrator and specialist agents
- `benchmark/` - benchmark task descriptions and annotation guidance
- `src/` - the minimal runnable prototype package
- `demo_data/` - seed data for the local prototype
- `assets/` - images used in repository presentation

## Runtime and deployment recommendation

ChemClaw-Lab is best understood as an **agent-oriented prototype built around an assistant runtime**, not just as a standalone Python package.

The author recommends using **OpenClaw** as the default deployment foundation, or another agent assistant framework with similar capabilities.

Why this matters:

- the project logic assumes messaging-native interaction
- the architecture expects orchestration across specialist agents
- local deployment becomes much easier when the runtime already supports messaging, tools, session context, and workflow automation

If you want to deploy or extend this project locally, it is strongly recommended that you:

1. install OpenClaw first, or choose a comparable agent assistant runtime
2. let that assistant help read this repository and explain the architecture
3. use the assistant to guide local setup and iterative implementation

For a more explicit deployment note, see [`docs/deployment_guidance.md`](docs/deployment_guidance.md).

## Start here

If you are opening the repository for the first time, read in this order:

1. [`docs/system_overview.md`](docs/system_overview.md)
2. [`docs/architecture.md`](docs/architecture.md)
3. [`docs/schema.md`](docs/schema.md)
4. [`docs/benchmark.md`](docs/benchmark.md)
5. [`docs/roadmap.md`](docs/roadmap.md)

Then use these supporting files:

- [`PROJECT_STATUS.md`](PROJECT_STATUS.md) for the current English summary
- [`PROJECT_STATUS_CN.md`](PROJECT_STATUS_CN.md) for the Chinese summary
- [`docs/deployment_guidance.md`](docs/deployment_guidance.md) for runtime and local deployment recommendations
- [`docs/next_steps.md`](docs/next_steps.md) for immediate implementation priorities
- [`docs/repository_structure.md`](docs/repository_structure.md) for repo organization notes

## Project status

This repository is currently in the **research design and repository bootstrapping phase**.

Already drafted:

- project positioning
- multi-agent architecture
- event-centric operational representation
- database schema draft
- benchmark design draft
- specialist agent prompt drafts
- benchmark and implementation-facing design materials
- early runnable prototype components

This is intentionally a docs-first repository at this stage.

## Minimal prototype now included

This repository now includes a first runnable prototype layer:

- a Python package scaffold in `src/chemclaw_lab/`
- a SQLite schema for core lab-operation entities
- a demo seed dataset in `demo_data/lab_seed.json`
- a small CLI for initializing, seeding, and inspecting demo data
- a smoke test in `tests/test_cli_smoke.py`

### Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
chemclaw init-db
chemclaw seed-demo
chemclaw status
chemclaw list-chemicals
chemclaw list-bookings

# optional: run tests
pip install -r requirements-dev.txt
pytest -q
```

## Suggested next implementation steps

1. add structured event ingestion from messages
2. add JSON schema validation for agent outputs
3. implement basic planning and conflict-check logic
4. add synthetic benchmark samples and evaluation scripts
5. expose the prototype through a minimal API or chat adapter
6. expand tests beyond smoke coverage

## Contributing

Contributions are welcome, especially around:

- markdown and documentation cleanup
- schema refinement
- synthetic benchmark examples
- evaluation design
- minimal prototype code

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

## Citation and reuse

If you reuse the ideas, structure, or benchmark framing from this repository in academic or open-source work, please cite or acknowledge the project once a formal release citation is available.

## License

This project is released under the [MIT License](LICENSE).
