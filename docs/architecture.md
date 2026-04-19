# Architecture

## High-level components

ChemClaw-Lab contains five major logical components:

1. **Messaging-facing layer**
2. **Orchestrator**
3. **Specialist agents**
4. **Audit / Confirmation layer**
5. **Dual-memory backend**

## 1. Messaging-facing layer

Receives:
- text messages
- images
- screenshots
- file descriptions
- mixed chat inputs

Typical channels:
- WeChat
- WhatsApp

Its job is to preserve the original evidence and normalize it for downstream processing.

## 2. Orchestrator

The Orchestrator:
- detects intent
- decomposes mixed requests
- routes subtasks
- merges outputs
- enforces event-first logic

It should never directly mutate operational state.

## 3. Specialist agents

### Agent A — Chemical & Consumable Manager
Focus:
- stock lookup
- location lookup
- usage / addition parsing
- restock suggestions

### Agent B — Experiment Memory Manager
Focus:
- project attribution
- sample attribution
- event extraction
- follow-up question generation
- weekly summary generation

### Agent C — Planning & Booking Manager
Focus:
- short-horizon plan generation
- dependency checking
- inventory-aware feasibility
- booking conflict detection
- alternative slot suggestion

## 4. Audit / Confirmation layer

Reviews risky or uncertain actions before they are applied.

Decision labels:
- `approve`
- `pending_confirmation`
- `reject`

## 5. Dual-memory backend

### Structured memory
Examples:
- users
- projects
- samples
- chemicals
- consumables
- inventory transactions
- experiment events
- bookings

### Unstructured memory
Examples:
- original messages
- image references
- screenshot descriptions
- file descriptions
- generated reports

## Event-first workflow

Raw message -> specialist parsing -> structured event -> audit / confirmation -> state update or summary / planning output

## Why this matters

This architecture makes it possible to:
- preserve evidence
- reduce unsupported writes
- coordinate across workflows
- benchmark the system
