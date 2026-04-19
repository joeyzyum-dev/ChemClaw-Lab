# Schema Specification (Condensed)

This file summarizes the operational schema for ChemClaw-Lab.

## Core entities

- `users`
- `projects`
- `samples`
- `chemicals`
- `consumables`
- `inventory_transactions`
- `experiment_events`
- `attachments`
- `instruments`
- `bookings`
- `purchase_requests`
- `message_logs`
- `audit_logs`

## Key principles

### Event-first
Messages must first become structured events.

### Raw evidence preserved
Messages and attachments remain stored as evidence.

### State is derived from approved events
Inventory and booking state should not be directly overwritten from casual chat.

## Core tables

### `users`
Lab members and roles.

### `projects`
Research projects and subprojects.

### `samples`
Lab-generated samples linked to projects.

### `chemicals`
Chemical inventory master records.

Suggested fields:
- names
- aliases
- CAS
- formula
- purity
- supplier
- location
- current amount
- threshold

### `consumables`
Non-chemical expendables such as separators, gloves, filters, vials.

### `inventory_transactions`
All stock-changing actions.

Important fields:
- item type
- item id
- transaction type
- amount delta
- unit
- project link
- confidence
- confirmation status

### `experiment_events`
Structured experiment memory records.

Typical event families:
- sample_preparation
- reaction
- characterization
- electrochem_test
- observation
- result
- issue
- failure
- decision
- next_step

### `bookings`
Internal instrument reservations.

### `audit_logs`
Trace of important actions and approval decisions.

## Base event schema

```json
{
  "event_id": "evt_20260414_0001",
  "event_type": "inventory_update",
  "event_subtype": "use",
  "timestamp": "2026-04-14T15:20:00+08:00",
  "reported_by": "user_001",
  "project_id": "proj_001",
  "sample_id": null,
  "raw_input": {
    "text": "I used 5 g KBr today"
  },
  "extracted_fields": {},
  "confidence": 0.95,
  "requires_confirmation": false,
  "status": "parsed"
}
```

## Main event families

### Inventory events
- use
- add
- adjust
- discard
- expire

### Experiment events
- observation
- characterization
- issue
- result
- next_step

### Planning / booking events
- booking_request
- conflict_detection
- planning_result

## Implementation note

A full SQL-style draft was already prepared in the design conversation and can be re-expanded later.
This file is the GitHub-friendly summary version.
