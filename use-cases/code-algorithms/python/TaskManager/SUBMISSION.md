# Task Manager Submission Summary

# 1. Initial vs. Final Understanding

Initial understanding:
- The project is a Python commandline task manager.
- It stores tasks in JSON and uses standard library modules only.
- The code is organized into CLI, business logic, storage, domain model, and helper modules.
- Tasks have title, description, due date, priority, status, and tags.

Final understanding:
- `cli.py` is the user entry point and dispatches commands to `TaskManager`.
- `TaskManager` orchestrates task creation, updates, retrieval, statistics, and export.
- `storage.py` handles JSON persistence and was extended to support CSV export.
- `models.py` contains the domain model, including `Task`, `TaskStatus`, and `TaskPriority`.
- Helper modules implement parsing (`task_parser.py`), priority scoring (`task_priority.py`), and merge logic (`task_list_merge.py`).
- Business rules are primarily in the domain model and service layer, with persistence kept separate.

2. Most Valuable Insights from Each Prompt

### Understanding Project Structure and Technology Stack
- Confirmed the layered architecture: CLI → service → storage → model.
- Identified the core technology stack as Python standard library only.
- Found inconsistencies between README command names and actual CLI commands.

### Finding Feature Implementation Locations
- Discovered there was no existing export or CSV feature.
- Confirmed the best feature location was `storage.py` for file output, with a wrapper in `TaskManager`.
- Determined that CLI needed an `export` subcommand.

 Understanding Domain Models and Business Concepts
- Extracted the core domain entities and business logic.
- Clarified that `Task` holds both state and metadata, while `TaskStatus` and `TaskPriority` define workflow and urgency.
- Highlighted domain questions around review status, tag behavior, and overdue semantics.

# Practical Application
- Converted domain understanding into implementation planning for a new business rule.
- Identified the files to modify and the likely place for the new abandonment logic.
- Clarified the need for team questions about priority semantics and automatic vs. manual rule execution.

3. Approach to Implementing the New Business Rule

Planned changes:
- Add `ABANDONED` to `TaskStatus` in `models.py`.
- Add a helper or rule method in `Task` or `TaskManager` to detect tasks overdue by more than 7 days.
- Implement `TaskManager.apply_abandonment_rule()` or similar to update task status and persist changes.
- Decide whether the rule should run on startup or via an explicit CLI command such as `cleanup`.
- Add tests for the new status, the rule logic, and persistence behavior.

Key considerations:
- Clarify whether both `HIGH` and `URGENT` should survive abandonment.
- Define if abandoned tasks remain recoverable or are treated as final.
- Confirm how the rule should interact with task statistics and overdue reporting.

 4. Strategies for Approaching Unfamiliar Code

Effective strategies:
- Start with the application entry point and follow the flow into the core service layer.
- Identify and document the main architectural layers before making changes.
- Use targeted searches for relevant keywords to find related functionality.
- Read the domain model closely to understand business rules and entity relationships.
- Inspect tests to learn expected behavior and edge cases.
- Keep a running written summary to capture insights and reduce confusion.

Future improvements:
- Run the application or sample commands early to confirm actual behavior.
- Look at available tests first for a behavior-driven view of the code.
- Use code navigation tools to trace definitions and references more quickly.
- Ask clarifying questions about ambiguous business rules before implementing changes.

 5.Next Implementation Steps
- Implement `TaskStatus.ABANDONED` and the overdue abandonment rule in `models.py` and `task_manager.py`.
- Add a CLI command or maintenance workflow to apply the abandonment rule explicitly.
- Extend unit tests to cover abandoned status, rule application, and persistence.
- Update `README.md` with any new CLI commands and examples.
- Run the full test suite to verify the new business rule and export behavior.
