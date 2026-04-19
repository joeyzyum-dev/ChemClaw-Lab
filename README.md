# ChemClaw-Lab

**ChemClaw-Lab** is a messaging-native, multi-agent assistant framework for chemistry laboratory operations.

It is designed for small academic chemistry labs where daily work is fragmented across chat apps, spreadsheets, screenshots, and informal notes. The project aims to turn those fragmented inputs into structured, traceable, and actionable laboratory memory for:

- inventory and consumable management
- experiment memory construction
- planning and internal instrument booking

The long-term goal is to make ChemClaw-Lab both:

1. a research project suitable for paper submission, and
2. a reusable open-source framework for AI-assisted laboratory operations.

---

## Core idea

Instead of forcing researchers to leave WeChat, WhatsApp, or similar tools, ChemClaw-Lab starts from the communication channels they already use.

Raw messages, images, and files are first converted into **structured events**, then used to update operational state, generate summaries, or coordinate bookings.

This gives the system four key properties:

- **messaging-native**
- **multi-agent**
- **event-centric**
- **traceable**

---

## Current project scope

ChemClaw-Lab currently focuses on a small chemistry lab setting:

- ~10 lab members
- internal instruments only
- existing chemical inventory table available
- target outcome: paper demo + benchmark + open-source starter framework
- orientation: research assistant for lab operations, not a general chatbot

---

## Main components

### Orchestrator
Routes user requests, decomposes mixed tasks, and coordinates specialist agents.

### Agent A: Chemical & Consumable Manager
Handles item lookup, stock queries, inventory updates, and restocking suggestions.

### Agent B: Experiment Memory Manager
Turns fragmented notes, photos, and screenshots into structured experiment memory and PI-facing summaries.

### Agent C: Planning & Booking Manager
Checks dependencies, plans short-horizon tasks, and coordinates internal instrument booking.

### Audit / Confirmation Layer
Prevents risky or uncertain writes from being silently applied.

---

## Why this project matters

Small academic labs often struggle with:

- delayed inventory updates
- fragmented experiment records
- weak visibility for PI supervision
- disconnected planning, inventory, and scheduling workflows

ChemClaw-Lab treats these as a single systems problem rather than isolated tasks.

---

## Repository guide

- `docs/` - architecture, schema, benchmark, roadmap, and project notes
- `agents/` - specialist agent prompt specifications
- `benchmark/` - benchmark task descriptions and annotation guidance
- `paper/` - paper outline and writing drafts
- `slides/` - one-page pitch material and figure prompts

---

## Suggested next implementation steps

1. create a synthetic lab environment
2. implement the event schema and SQLite backend
3. connect a basic messaging interface
4. prototype Agent A/B/C with schema-constrained outputs
5. build ChemLabOps-Bench v1
6. run baseline experiments
7. write the first paper draft

---

## Status

This repository starter was generated from an extended design conversation and already includes:

- system concept
- architecture
- schema draft
- benchmark draft
- agent prompt drafts
- paper outline
- interview one-pager notes

It is intentionally documentation-heavy at this stage.
