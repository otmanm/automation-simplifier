---
name: automation-simplifier
description: Use when someone brings an app, paid service, repository, workflow, or idea and wants viable ways to automate or simplify it, reduce runtime AI or tokens, or spend less attention operating it.
---

# Simplify an automation

Aim for a finished workflow that achieves the user's outcome with zero runtime AI and model tokens whenever feasible. AI can help investigate and build it. Optimize the attention required to get an acceptable result, including recovery when something goes wrong.

## 1. Understand what the user brought

Start with the supplied link, local artifact, screenshot, description, or desired result. Reuse relevant prior research. Inspect what the user has already provided before asking for more. For an app, use public product material and authorized observations. For a repo or script, follow the documented entry point into relevant code, configuration, dependencies, and reuse license. For an existing automation, look for its trigger, settings, and execution records. Treat a screenshot as evidence of the visible state. For an idea, identify the current manual route if known and label imagined behavior as proposed.

When no workflow is named, map the product first. Give its main user-visible capabilities, what each achieves, and the source and limits of that coverage. Distinguish provider claims, inspected code, observed behavior, inference, and unknowns. A paid product's visible behavior can establish a capability while its internal mechanism remains unknown. Stay within authorized access. Purchases or private uploads need specific permission. Derive alternatives from functional requirements and respect reuse licenses and proprietary visual designs.

Briefly restate the goal in the user's terms. If selecting a workflow or resolving an unknown would materially change the outcome, quality, authority, or burden, ask the one question that settles the next decision. Otherwise proceed with the stated scope and disclose material assumptions.

## 2. Trace what actually happens

Choose one representative input and define what the user would accept as success. Follow it from trigger through the user finding and using the result. Use the available UI, source, documentation, or trace to reconstruct the sequence. Follow a material exception such as a conflicting record through detection, recovery, or a visible stop. If no baseline is available, say so. Label proposed or unobserved paths throughout.

Split a step where an actor or dependency takes over, a decision changes the outcome, the user must intervene, or a failure needs different recovery. Group internal operations that have the same effect on the decision. For each meaningful step record its input, executor and action, output, evidence, what it protects, and what the user must click, read, decide, wait for, or correct. Distinguish fixed rules, human judgment, model inference, and unknown mechanisms. Identify changing external inputs independently of the rule that reads them. Mark an unclear purpose unknown.

For each step you would remove, combine, automate, or move into the background, name the problem it currently catches, where that protection goes, and a case that would expose its loss. For example, automatically skip an identical duplicate, but surface two records with the same ID and different contents. Check both outcomes before claiming duplicate handling is preserved.

## 3. Compare complete alternatives

Compare today's route with genuinely different viable options on the **same input, exception, success criterion, and constraints**. Consider keeping or configuring the original, reusing a component, connecting existing tools, or building the missing part. Reuse prior findings and investigate gaps only if they could change the choice. Include how each route starts, delivers a usable result, and recovers. Identify lost capabilities, dependencies or network use, maintenance, and who absorbs any extra work.

Screen first for the required outcome, authority, and acceptable quality. Then weigh runtime model dependence against actual attention and rework. If rules leave ambiguous cases, consider a bounded human decision. Only include a model-assisted route as eligible when the user's constraints permit it. If no route satisfies a hard requirement, show the unmet requirement and the specific tradeoff that would need a decision.

For a zero-AI requirement, check the trigger, launcher or scheduler, routing, processing, validation, retry, fallback, and recovery, including dependencies that can invoke models. Local inference, including model-based OCR, counts as AI. A silent fallback to an agent disqualifies the route. Evaluate network independence, repeatability under stated conditions, and output correctness separately. Report what inspection establishes, what a run demonstrates, and what remains unknown. A successful offline run alone cannot exclude local inference.

## 4. Compare and try

Give the user one short before-and-after comparison in operational terms. Show what they do on a normal run, what interrupts them on the exception, what changed protections catch, and why one option fits. Identify any material decision that remains. Label measurements, estimates with a stated basis, and unknowns for attention, elapsed time, coverage, and cost. Avoid invented savings and determinism percentages.

When implementation is requested and authorized, deliver the smallest reversible result that works through the intended entry point, independently of the building agent. Verify the outcome and changed protections on the common cases. For a claimed runtime restriction, state what was actually enforced or observed and which paths were covered. Reuse the user's feedback if they have already tried the same flow and build. Otherwise offer one real use when ready and report that trial as pending until it occurs. Keep implementation checks and the user's experience as distinct findings.
