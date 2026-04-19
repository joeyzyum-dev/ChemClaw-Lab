# System Overview

## Project statement

ChemClaw-Lab is a messaging-native multi-agent framework for chemistry laboratory operations.

It aims to convert fragmented communications into:

- structured inventory state
- structured experiment memory
- executable plans
- traceable laboratory summaries

## Problem background

In many chemistry labs, important operational information is scattered across:

- WeChat / WhatsApp messages
- Excel sheets
- screenshots
- experiment photos
- informal short notes

This leads to:

- outdated stock records
- poor project visibility for PI
- hard-to-reconstruct experiment timelines
- disconnected planning and scheduling

## System goal

Support daily laboratory operations without requiring users to leave their habitual communication channels.

## Main workflows

1. **Inventory operations**
   - where is a reagent?
   - how much is left?
   - I used 5 g of KBr today
   - what should we restock?

2. **Experiment memory construction**
   - convert fragmented notes and images into structured events
   - connect those events to projects and samples
   - generate daily/weekly summaries

3. **Planning and booking**
   - plan what should be done next
   - check resource availability
   - coordinate internal instrument booking

## Core design choices

### Messaging-native
The system begins from real lab communication rather than forcing a new interface.

### Event-centric
Messages do not directly update state. They first become structured events.

### Multi-agent
Different specialist agents handle different operational workflows.

### Traceable
Important outputs should be grounded in messages, events, and state.
