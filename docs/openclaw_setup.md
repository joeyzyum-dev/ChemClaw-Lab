# OpenClaw Setup Guide

This document explains a practical way to explore and extend ChemClaw-Lab with **OpenClaw** as the recommended assistant runtime.

## Why use OpenClaw here

ChemClaw-Lab is not only a Python prototype. Its real value comes from the combination of:

- messaging-native workflows
- multi-agent orchestration
- structured event generation
- iterative assistant-guided development

OpenClaw already provides much of the surrounding runtime needed for this style of project.

## Recommended use cases

Using OpenClaw is especially helpful when you want to:

- read and summarize the repository with an AI assistant
- understand the architecture and schema before coding
- turn design notes into implementation tasks
- incrementally build local prototype features
- connect the project to future message-driven workflows

## Suggested local workflow

### 1. Install OpenClaw

Install and configure OpenClaw first.

If you are new to OpenClaw, consult the official documentation first:

- OpenClaw docs: <https://docs.openclaw.ai>
- OpenClaw source: <https://github.com/openclaw/openclaw>

### 2. Clone this repository locally

```bash
git clone https://github.com/joeyzyum-dev/ChemClaw-Lab.git
cd ChemClaw-Lab
```

### 3. Ask your OpenClaw assistant to read the repository in order

A good reading order is:

1. `README.md`
2. `docs/index.md`
3. `docs/system_overview.md`
4. `docs/architecture.md`
5. `docs/schema.md`
6. `docs/deployment_guidance.md`
7. `docs/next_steps.md`

### 4. Use the assistant as a deployment and coding copilot

Examples of good requests:

- "Read this repository and explain the architecture in plain language."
- "Summarize what is already implemented versus what is still conceptual."
- "Help me run the minimal prototype locally."
- "Turn the next steps into a concrete implementation plan."
- "Add a message-to-event parser for the prototype."

### 5. Use OpenClaw to keep implementation aligned with project logic

As the repository grows, OpenClaw can help with:

- code edits
- schema iteration
- benchmark preparation
- documentation maintenance
- local automation and test runs

## Recommended mindset

Treat OpenClaw as the working layer around ChemClaw-Lab, not just as an optional helper.

That approach fits the spirit of this repository better than reading the docs in isolation and manually stitching everything together.

## Minimal local prototype commands

If your assistant asks you to run the current prototype manually, these are the core commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
chemclaw init-db
chemclaw seed-demo
chemclaw status
chemclaw list-chemicals
chemclaw list-bookings
```
