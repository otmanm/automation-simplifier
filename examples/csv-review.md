# Worked example — review only conflicting records

An operator imports a CSV. They need a saved copy and want to make the final decision when two rows disagree. The [fictional fixture](csv-kit/README.md) includes an identical `A01` repeat and two `B02` rows with quantities of `6` and `9`.

To try the skill, open the fixture in your agent and invoke Automation Simplifier. Ask what the product does and how to reduce review prompts while keeping control of conflicts and saving a new CSV. A good response should read the fixture and distinguish the current behavior from its proposal.

| What the operator needs to protect | Current workflow | Proposed workflow |
| --- | --- | --- |
| A valid input | Check for the expected CSV columns. | Keep the check and show a clear error for a bad header. |
| Identical `A01` rows | Ask which row to keep. Both rows contain the same data. | Keep one copy automatically once the rows match exactly. |
| `B02` values of `6` and `9` | Ask the operator which row to keep. | Keep the decision with the operator and show both values. |
| A safe output | Write a new CSV and refuse to replace an existing output. | Keep exclusive creation. If the destination exists, prompt for a different name. |

If this is the only change and the owner already agrees on the duplicate rule, editing the importer directly is a reasonable route. The skill is useful when the operator still needs help comparing options or deciding which checks to preserve.

**One trial to accept the change.** On the same batch, check that `A01` produces no review prompt and `B02` produces one. Try a bad header and an existing output. Stop during review and confirm that no incomplete output is treated as finished. A completed CSV must contain the selected records and leave existing files untouched. Run the resulting importer directly if its runtime is meant to use zero model calls.

This is a walkthrough of a proposed change. The fixture still contains the original behavior. The example makes no claim about time savings in production.
