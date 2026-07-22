---
name: persistent-python
description: The persistent clikernel Python session — Jeremy's preferred single tool for nearly ALL Python work. TRIGGER — read and bootstrap as step zero of EVERY session where clikernel is available, before the first tool call: even tasks that only read a file or search a directory, plus stateful inspection, editing code or notebooks, debugging, experiments, API probes, data transforms, pyskills discovery, notebook-style work, local tool orchestration. If it could go through Python, it goes here — never python -c, Bash heredocs, or ad hoc scripts.
---

# Persistent Python

ALWAYS use the `clikernel` MCP server for ALL Python work: writing code, editing code or notebooks, running or debugging anything, inspecting objects or packages, probing APIs, and transforming data. It is the workbench for every task in this environment. If the work could go through Python, it goes through clikernel. Do not fall back to `python -c`, shell heredocs, or ad hoc scripts.

The server's `execute` tool runs code in one persistent IPython session, so imports, variables, monkeypatches, and cached objects carry across calls. Check the clikernel MCP server instructions already in your context before the first call. Normally the startup script has run, and its output says what is imported and which cells to run next. Follow it. If the instructions report that project imports were skipped, or contain no startup output, report that to the user before other work. Then run the guarded import block from `$XDG_CONFIG_HOME/clikernel/startup.py` (default `~/.config/clikernel/startup.py`) as one `execute` call. That file is the single source of truth for bootstrap imports; never retype them from memory.

Complete every practice task named in the server instructions (the llmdojo round started by `dojo_start()`) before any other work. This gate applies in every session, including tasks that only read files or search directories.

The server instructions and startup docs cover the tools, notebook magics, output shape, interaction rules, reload gotchas, and pyskills workflow, so this skill does not repeat them. `list_pyskills()` shows the available tooling. Prefer a relevant pyskill over ad hoc code.

## Environment specifics

The following apply specifically to this environment:

- Doc-state persists on disk per conversation and is managed mechanically (the compaction hook resets it when your context is rewritten), so there is nothing to run by hand: doc notes fire exactly for the functions whose docs you don't hold. After a kernel restart or compaction, just read `doc(f)` again whenever a note fires.
- Use `exhash` for ALL edits -- code, tests, config, prose, notebook cells -- never the host's built-in file-edit tools, and read with `lnhashview_*` (not the host's file reader) the moment an edit is plausible. `llmsurgery.dlgskill` covers the structural cell/message operations exhash doesn't; `fastcore.tools` file editors are the rare fallback where exhash can't express a text edit.
- Codex settings are TOML: `~/.codex/config.toml` is user-global, while trusted `.codex/config.toml` files apply from the project root down to the current directory, with the closest project file winning. CLI overrides have higher precedence. Hooks can live in `hooks.json` or inline `[hooks]` tables at user and project config layers; matching hooks from every active layer are merged. `PreToolUse` can inspect, deny, or rewrite Bash, `apply_patch`, MCP, and most other local tool calls. `[[skills.config]]` entries enable or disable skills by path, while `mcp_servers.<id>.enabled_tools` and `disabled_tools` control which MCP tools are exposed. Do not disable Bash or `apply_patch` merely because clikernel is preferred; first establish that sessions misuse them. Config changes take effect after restarting Codex.
