# Project Status

## Current stage

This project is currently in the **research design and repository bootstrapping phase**.

The following have been drafted:

- project positioning
- multi-agent architecture
- event-centric operational representation
- database schema
- benchmark design
- agent prompt specifications
- paper structure and early writing draft
- one-page PhD interview slide concept

## What is already defined

### Product / research positioning
ChemClaw-Lab is framed as:

> a messaging-native, event-centric multi-agent framework for chemistry laboratory operations

### Deployment assumptions
- lab size: around 10 members
- current data source: chemical inventory Excel
- booking scope: internal lab instruments
- research target: demo + benchmark + paper
- assistant orientation: research assistant for lab operations

### Target outputs
- reusable open-source project
- benchmarkable system
- paper submission candidate
- one-page interview narrative

## Immediate next tasks

### Engineering
- implement SQLite schema
- import a synthetic or real inventory table
- define JSON schemas for event outputs
- create basic evaluation scripts

### Data
- construct a synthetic lab environment
- build benchmark examples for the 5 task families
- define annotation format and train/val/test split

### Research
- refine benchmark metrics
- prepare baseline systems
- collect case studies
- continue paper drafting

## Risks to manage
- scope becoming too large too early
- too much focus on prompts without data and evaluation
- unclear boundary between lab operations and scientific reasoning
- overclaiming before implementation

## Guiding principle
Do not try to build a fully general AI lab platform first.
Start with a clear, credible, small-lab operations assistant.
