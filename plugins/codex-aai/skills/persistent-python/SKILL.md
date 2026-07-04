---
name: persistent-python
description: The preferred single tool to use for nearly all tasks that can be advanced through live Python execution, including stateful inspection, file-editing workflows, debugging, experiments, API probes, data transforms, pyskills discovery, notebook-style work, and local tool orchestration through a persistent clikernel session.
---

# Persistent Python

ALWAYS use a persistent background `clikernel` process for ALL Python work: writing code, editing code or notebooks, running or debugging anything, inspecting objects or packages, probing APIs, transforming data. It is the workbench for every task in this environment, not a tool you reach for occasionally -- if what you're doing could go through Python, it goes through clikernel. Do not fall back to `python -c`, shell heredocs, or ad hoc scripts.

`clikernel` runs IPython-compatible code from stdin in one persistent session (state carries across requests), and everything else here builds on that. So your first use of it in every session is to bootstrap the rest: execute the following (as one multiline request), then follow the instructions it prints:

```python
from pyskills import list_pyskills, doc
import clikernel.skill, pyskills.skill
print(doc(clikernel.skill))
print(doc(pyskills.skill))
list_pyskills()
```

Those docs cover the CLI delimiter protocol, output shape, interaction rules, reload gotchas, and the pyskills workflow, and are not repeated here; `list_pyskills()` shows what tooling is available -- always prefer a relevant pyskill over ad hoc code.

## Driving clikernel from Codex

The instructions above ship with `clikernel` itself and are portable. The following is specific to running it from Codex:

- Work through ONE persistent `clikernel` process in a background PTY session. If one is already running for this conversation, keep using it; otherwise start `clikernel` as a PTY background session, normally with elevated permissions when the user wants access to global skill files or other paths outside the current workspace. Do not start extra Python processes unless `clikernel` is broken or the user explicitly asks, and do not close the process just for cleanup -- leave it available for future turns.
- After a user closes and resumes a Codex session, the old background terminal may be gone without notification. If `write_stdin` returns `Unknown process id`, start a fresh `clikernel` process and redo imports, monkeypatches, and other required state.
- The bundled wrapper `scripts/clikernel_repl.sh` (resolve relative to this skill directory) is an alternative if state dirs in writable tmp folders are needed.
- When using `exec_command` / `write_stdin` with `clikernel`, raise the tool-result limit and use a practical yield: `{"max_output_tokens": 50000, "yield_time_ms": 1000}`. For quick requests, `yield_time_ms=1000` usually captures the acknowledgement and whole framed response. For long-running code, use `write_stdin(chars="")` with a longer timeout to read pending output without queueing another request.
- Output tokens cost much more than input tokens -- be surgical about what you print.

## Environment specifics

- The env is pre-configured with every project being worked on already installed via `pip install -e`. Do *NOT* use `sys.path.insert` for any reason -- whatever module you need should already be importable. If it isn't, STOP and ask the user rather than patching the path.
