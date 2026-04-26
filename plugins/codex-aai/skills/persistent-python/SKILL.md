---
name: persistent-python
description: The preferred single tool to use for nearly all tasks that can be advanced through live Python execution, including stateful inspection, file-editing workflows, debugging, experiments, API probes, data transforms, pyskills discovery, notebook-style work, and local tool orchestration through a persistent clikernel session.
---

# Persistent Python

## Core Idea

Use a persistent background `clikernel` process as the default tool workspace. This is the preferred single tool for nearly all Python-capable tasks because it keeps state across the conversation: imports, live objects, inspected docs, monkeypatches, cached results, API clients, and small experiments.

Think of the session as the agent's notebook-style workbench. Prefer it over one-off Python scripts when you need to inspect runtime behavior, test ideas, call Python APIs, use pyskills, examine package state, run live probes, work through file-editing logic, or iterate on an implementation detail. Shell commands are still fine for file search, git, project test commands, and non-Python tools.

`clikernel` is a small PyPI module available in this environment. It wraps `execnb.shell.CaptureShell`, runs IPython-compatible code from stdin, and uses a ready delimiter protocol. This gives a cleaner persistent Python process than an interactive terminal REPL: no echoed input, no prompt parsing, and no `%cpaste` dance.

## Start Or Reuse

Always work through one persistent `clikernel` process in a background PTY session. If one is already running for this conversation, keep using it; otherwise start one with:

```bash
clikernel
```

Start it as a PTY background session, normally with elevated permissions when the user wants access to global skill files or other paths outside the current workspace. `clikernel` sets safe default state directories when needed and disables terminal echo when stdin is a TTY. The normal home IPython/matplotlib dirs are expected to be writable in this environment, and execnb avoids importing matplotlib during startup.

Do not start extra Python processes for this workflow unless `clikernel` is broken or the user explicitly asks. Do not close the process just for cleanup; leave it available for future turns. After a user closes and resumes a Codex session, the old background terminal may be gone without a proactive notification. If `write_stdin` returns `Unknown process id`, start a fresh `clikernel` process and redo imports, inspected docs, monkeypatches, and other required state.

The bundled `clikernel` wrapper is an alternative if state dirs in writable tmp folders are needed. Resolve this path relative to this skill directory:

```bash
scripts/clikernel_repl.sh
```

## Protocol

On startup, `clikernel` prints loading status followed by a fresh ready delimiter. The delimiter is always `--` plus 5 alphanumeric characters:

```text
please wait, loading...
loading complete. first delimiter:
--aB3x9
```

Any startup warnings are printed before the first delimiter.

Treat that delimiter as both the readiness signal and the current multiline terminator.

Send a single line to execute a single-line request:

```text
1+1
```

The response body is printed, followed by a new ready delimiter:

```text
2
--Q7z2M
```

Use a bare `--` line to start multiline input. End the block with the latest ready delimiter exactly:

```text
--
def f(x):
    return x + 1

f(2)
--Q7z2M
```

The output is followed by a fresh delimiter:

```text
3
--mN8pA
```

Treat the new delimiter line as the completion signal. Do not look for an IPython prompt. Do not use `%cpaste` with `clikernel`. Do not invent your own request id or terminator.

Python exceptions are rendered as normal notebook error output. Protocol/worker failures are rendered with readable XML-ish error tags, then followed by a fresh delimiter.

## Output Shape

`clikernel` renders notebook outputs with `fastcore.nbio.render_text`.

If there is exactly one non-empty stream, display object, execute result, or error, the body is just the preferred text form:

```text
42
--Q7z2M
```

For multiple non-empty outputs, the body uses readable XML-ish tags with raw, unescaped body text:

```text
<stream name="stdout">
hello
</stream>
<display_data mime="text/markdown">
**shown**
</display_data>
<execute_result mime="text/plain">
42
</execute_result>
--Q7z2M
```

For `display_data` and `execute_result`, `render_text` chooses a non-image MIME representation with `html1st=False`, so markdown is preferred over HTML and images are ignored in concise text mode. If you need rich binary output, save it to a file or inspect a smaller textual representation.

## Interaction Rules

When using `exec_command` / `write_stdin` with `clikernel`, raise the tool-result limit and use a practical yield:

```json
{"max_output_tokens": 50000, "yield_time_ms": 1000}
```

For quick requests, `yield_time_ms=1000` is usually enough to receive the whole framed response. For long-running code, set a longer yield up front. Avoid sending extra blank lines just to poll: a newline is a real single-line request in `clikernel`.

Keep probes compact. Catch expected exceptions and print only the relevant summary instead of letting long tracebacks or HTML bodies fill the terminal:

```python
try: print("OK", summary)
except Exception as e: print("ERR", type(e).__name__, str(e)[:300])
```

Use raw triple-quoted strings by default for generated Markdown, docs, code snippets, regexes, commands, or examples:

```python
content = r"""
print('\n'.join(items))
cmd = 'file:$a\nnew line'
"""
```

Most multiline strings in this workflow are source artifacts where backslashes should be preserved. Use normal triple-quoted strings only when Python escape interpretation is deliberate. For nontrivial generated text, verify risky lines with `repr(...)`, a focused readback, or a small slice view before broad writes.

Try the simple import or API call first before mutating environment, monkeypatching, or adding setup. Change session state only after the ordinary path fails and the reason is understood.

For file-editing workflows, view the target slice first and make the smallest verified edit that handles the change. Avoid whole-file rewrites when a line/range/string operation is enough. For complex text edits, prefer exhash because it verifies line addresses and can apply multi-file writes atomically.

## Critical Issues

- Do *NOT* re-run `import` statements that you have previously run in this session. It is persistent, so once run, the import is done. Use `importlib.reload` if you modify a module and need to reload it.
- Do *NOT* use `sys.path.insert` for any reason, ever. The environment is pre-configured with all projects being worked on already installed with `pip install -e`. All needed modules should already be in the env.
- If the env is missing a needed module, STOP and ask the user.
- Output tokens cost much more than input tokens. Aim for surgical use of tools/functions: inspect only the needed docs or lines, and do not dump large values unless the user asks.
- Default to raw triple-quoted strings `r"""..."""` for most generated source artifacts. Avoid `'\n'` in strings when real newlines are clearer.

## Pyskills

Pyskills are Python capabilities available inside this persistent workspace. Discover them from `clikernel`:

```python
from pyskills import list_pyskills, doc
list_pyskills()
```

Orient with the core docs:

```python
import pyskills.skill
doc(pyskills.skill)
```

Before using a candidate pyskill, import it and inspect the module or specific callable:

```python
from pyskills import edit
doc(edit)
```

Run `doc(skill_module)` by itself as the first inspection step. After the module docs are clear, inspect individual functions or classes as needed.

Always inspect individual functions or classes with `doc(symbol)` before calling them. Summarize pyskills output to the user; do not dump full docs or large return values unless asked.

For notebook work, prefer `pyskills.edit.view_nb` and related notebook APIs. `view_nb` shows the authored notebook source in the form a human is meant to read.
