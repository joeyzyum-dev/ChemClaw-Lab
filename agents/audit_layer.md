# Audit & Confirmation Layer

## Purpose
Review risky, ambiguous, or high-impact actions before they are applied.

## Decision labels
- approve
- pending_confirmation
- reject

## Review criteria
- identity certainty
- amount plausibility
- unit completeness
- evidence sufficiency
- conflict with verified state
- operational risk level

## Example output

```json
{
  "decision": "pending_confirmation",
  "risk_level": "high",
  "reason": "Hazardous chemical usage has missing unit and uncertain project attribution.",
  "required_action": "confirm_unit_and_project"
}
```

## Typical triggers
- hazardous chemical deductions
- destructive inventory corrections
- missing unit with operational impact
- overlapping booking requests
- unsupported summary claims
