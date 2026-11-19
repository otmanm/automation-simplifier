# Automation Simplifier

Bring an app, a repository, or a recurring workflow. Automation Simplifier helps you see what happens today, what each check protects, and which changes could reduce model calls or the decisions you have to make.

The skill uses the model in your agent to investigate and compare options. Use material your model provider is authorized to receive. A finished workflow can run directly with zero model calls when its rules and checks are implemented in ordinary software. The experience and runtime still need to be tested for each workflow.

## Try it

1. Open your agent in the project with the workflow, or give it a link and say which outcome matters. If you are unsure which feature to focus on, ask it to map the product first.
2. Invoke the skill with the command for your agent below. Give it an ordinary example and an exception, such as two rows with the same ID and different values.
3. Read the proposed before-and-after. You should see what becomes automatic, what still needs your decision, and how to check that the result still does the job.

Start with the [worked CSV example](examples/csv-review.md). It uses fictional data and walks through the different treatment of identical and conflicting records. The accompanying fixture is the original workflow for inspection.

## Installation

The portable folder is `skills/automation-simplifier/`. It contains `SKILL.md` and its MIT notice. To get a fixed version, download `automation-simplifier-v0.1.0.zip` from the GitHub release and extract the folder.

| Agent | Install and invoke |
| --- | --- |
| Codex | Copy the folder into your project's `.agents/skills/` or your personal `~/.agents/skills/`. Open Codex in the project and type `$automation-simplifier` with the request. |
| Hermes | In Terminal, run `hermes skills install otmanm/automation-simplifier/skills/automation-simplifier` to install from the repository's default branch. For the fixed version, copy the extracted folder into the `skills/` directory of your active Hermes profile (`~/.hermes/skills/` for the default profile). In a fresh Hermes chat, type `/automation-simplifier` with the request. |
| Claude Code | Copy the folder into your project's `.claude/skills/` or your personal `~/.claude/skills/`. Open Claude Code and type `/automation-simplifier` with the request. **Documented, test pending.** |
| Hosted Claude | In Claude's **Customize → Skills**, choose **Upload a skill** and select the ZIP. Enable it and ask Claude to use Automation Simplifier. **Documented, test pending.** [Claude's upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |

## Release evidence

- **Codex** — The exact skill file passed the format check and one explicit invocation covering three cases. These covered a PDF workflow, a CSV review, and ambiguous request routing.
- **Hermes** — Local discovery and one read-only CSV review passed in Hermes v0.23.2 using the explicit skill preload. The tagged release notes will record the public GitHub install check.
- **Claude Code and hosted Claude** — Both installation routes are documented. The skill has not yet been tested in either host.

The worked CSV example is a walkthrough. Its reduction from two review prompts to one is an expected result for that fixture after implementing the proposed rule.
