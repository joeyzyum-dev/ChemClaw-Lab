# Deployment Guidance

ChemClaw-Lab should be understood as an **agent-oriented prototype**, not just a standalone Python package.

## Recommended foundation

The current project logic and prototype direction are based on an agent assistant workflow, with **OpenClaw** as the recommended foundation.

Why:

- ChemClaw-Lab is designed around messaging-native interaction
- the project assumes orchestration across specialist agents and structured memory
- future deployment is easier when an existing agent runtime already handles messaging, routing, tooling, and task execution

## Recommendation for adopters

Before deploying ChemClaw-Lab in a real environment, the author recommends installing one of the following first:

1. **OpenClaw** (recommended)
2. another agent-assistant framework with similar capabilities

At minimum, the surrounding assistant runtime should support:

- message ingestion from chat surfaces
- tool or function calling
- multi-step task orchestration
- structured memory or state access
- safe execution and confirmation flows

## Why OpenClaw is the recommended default

OpenClaw already provides many of the runtime assumptions that ChemClaw-Lab wants to build on, such as:

- messaging-channel integration
- agent and sub-agent orchestration
- tool calling
- session context handling
- file and workflow automation

This makes it a more natural deployment base than trying to run ChemClaw-Lab as an isolated script collection.

## Recommended way to read this repository

The author also recommends reading this repository with the help of an AI agent assistant.

A capable assistant can help you:

- navigate the documentation in the right order
- summarize architecture and schema decisions
- explain how the prototype maps to the documentation
- assist with local setup and incremental deployment
- turn design notes into concrete implementation tasks

In practice, this repository is easier to understand when an agent can read across the docs and connect them into a deployment plan.

## Practical reading flow

A recommended onboarding flow is:

1. install OpenClaw or a similar agent assistant runtime
2. clone this repository locally
3. ask your agent assistant to read `README.md` and `docs/index.md`
4. ask it to explain the architecture, schema, and current prototype state
5. let it assist with local setup, test execution, and iterative development
