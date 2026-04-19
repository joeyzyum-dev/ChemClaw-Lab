# Repository Structure

This repository is intentionally documentation-first at the current stage.

## Top-level folders

- `agents/` - formal role and prompting drafts for the orchestrator and specialist agents
- `benchmark/` - benchmark framing, task descriptions, and annotation notes
- `docs/` - system overview, architecture, schema, roadmap, and open-source strategy
- `paper/` - early paper outline and draft text
- `slides/` - one-page pitch material and figure prompt notes

## Why this structure

ChemClaw-Lab is currently in the research design and prototype planning phase. A documentation-heavy layout helps:

1. preserve project framing and scope
2. keep architecture decisions explicit
3. make future implementation work easier to track
4. support paper writing and open-source release preparation

## Planned future additions

As the project moves into implementation, the repository is expected to add folders such as:

- `src/` or `app/` for core code
- `data/` or `demo_data/` for synthetic lab environments
- `scripts/` for evaluation and data processing utilities
- `tests/` for schema and workflow validation
