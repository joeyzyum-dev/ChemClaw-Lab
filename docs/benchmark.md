# ChemLabOps-Bench

ChemLabOps-Bench is a benchmark suite for messaging-native laboratory operation assistants.

## Motivation

We do not want ChemClaw-Lab to remain only a demo.  
We want a benchmark that tests whether the system can actually perform useful lab-operation tasks.

## Benchmark goals

Evaluate whether the system can:

1. understand inventory questions
2. parse inventory-changing actions
3. structure fragmented experiment notes
4. generate grounded project summaries
5. produce executable plans and valid booking suggestions

## Shared environment

The benchmark assumes a small chemistry lab environment containing:

- users
- projects
- samples
- chemicals
- consumables
- instruments
- bookings
- inventory transactions
- message logs

## Task families

### Task A — Inventory QA
Input: natural-language inventory question  
Output: correct item, location, quantity, or clarification

### Task B — Inventory Update Parsing
Input: usage / addition / correction statement  
Output: structured inventory event

### Task C — Experiment Log Structuring
Input: fragmented messages + attachment descriptions  
Output: structured experiment events + follow-up need

### Task D — Weekly Project Summary
Input: event stream over a time window  
Output: evidence-grounded PI-facing summary

### Task E — Planning and Booking
Input: user goal + project/sample/inventory/schedule context  
Output: feasible plan, blockers, and booking suggestion

## Key evaluation dimensions

- correctness
- executability
- faithfulness
- ambiguity handling
- confirmation logic
- traceability

## Suggested metrics

### Inventory QA
- item identification accuracy
- location accuracy
- quantity accuracy
- ambiguity handling accuracy

### Inventory Update Parsing
- item extraction F1
- amount accuracy
- unit normalization accuracy
- project attribution accuracy
- confirmation decision accuracy

### Experiment Log Structuring
- event type F1
- slot extraction F1
- condition completeness
- project accuracy
- sample linking accuracy
- follow-up recall / precision

### Weekly Summary
- factual consistency
- evidence coverage
- unsupported claim rate
- issue recall
- usefulness

### Planning and Booking
- plan executability accuracy
- dependency checking accuracy
- inventory sufficiency accuracy
- conflict detection accuracy
- booking validity

## Baselines

1. rule-based system
2. single generalist agent
3. multi-agent without event-centric memory
4. full ChemClaw-Lab

## Why the benchmark matters

The benchmark is part of the research contribution, not just an evaluation add-on.
It helps position ChemClaw-Lab as a benchmarkable operational research system.
