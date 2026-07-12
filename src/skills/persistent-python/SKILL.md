---
name: persistent-python
description: The persistent clikernel Python session — Jeremy's preferred single tool for nearly ALL Python work. TRIGGER — read and bootstrap as step zero of EVERY session where clikernel is available, before the first tool call: even tasks that only read a file or search a directory, plus stateful inspection, editing code or notebooks, debugging, experiments, API probes, data transforms, pyskills discovery, notebook-style work, local tool orchestration. If it could go through Python, it goes here — never python -c, Bash heredocs, or ad hoc scripts.
---

# Persistent Python

<!-- claude -->
ALWAYS use the `clikernel` MCP server for ALL Python work: writing code, editing code or notebooks, running or debugging anything, inspecting objects or packages, probing APIs, transforming data. It is the workbench for every task in this environment, not a tool you reach for occasionally -- if what you're doing could go through Python, it goes through clikernel. Do not fall back to `python -c`, Bash heredocs, or ad hoc scripts.

The server's `execute` tool runs Python code in one persistent IPython session (state carries across calls), and everything else here builds on that. So your first use of it in every session is to bootstrap the rest. But first check the clikernel MCP server instructions already in your context: a startup script may have run, and its printed output there tells you what's already imported -- if it printed a bootstrap snippet, run that snippet rather than re-importing. Otherwise execute the following two cells, then follow the instructions they print:

```python
from pyskills import list_pyskills, doc
import clikernel.skill as clik, pyskills.skill as pysk, pyskills.edit as pyse, exhash.skill as exh
from pyskills.edit import *
from exhash.skill import *
doc(clik, pysk, pyse, exh)
```

then, as a second cell (only a cell's last expression displays, so two displays means two cells):

```python
list_pyskills()
```

Then complete ALL practice tasks mentioned in the server instructions (the clikernel dojo: `from clikernel.dojo import *; dojo_start()`) before any other work. This is an unconditional gate in EVERY session -- including ones that only read files or search directories -- and no softer phrasing anywhere ('to practice...') makes it optional.

Those docs cover the tools, notebook magics, output shape, interaction rules, reload gotchas, and the pyskills workflow, and are not repeated here; `list_pyskills()` shows what tooling is available -- always prefer a relevant pyskill over ad hoc code.
<!-- /claude -->
<!-- codex -->
ALWAYS use a persistent background `clikernel` process for ALL Python work: writing code, editing code or notebooks, running or debugging anything, inspecting objects or packages, probing APIs, transforming data. It is the workbench for every task in this environment, not a tool you reach for occasionally -- if what you're doing could go through Python, it goes through clikernel. Do not fall back to `python -c`, shell heredocs, or ad hoc scripts.

`clikernel` runs IPython-compatible code from stdin in one persistent session. On first use in every session, follow any bootstrap instructions printed at startup. Otherwise execute this as one multiline request:

```python
from pyskills import list_pyskills, doc
import clikernel.skill as clik, pyskills.skill as pysk, pyskills.edit as pyse, exhash.skill as exh
from pyskills.edit import *
from exhash.skill import *
doc(clik, pysk, pyse, exh)
list_pyskills()
```

Then complete ALL practice tasks printed at startup (the clikernel dojo: `from clikernel.dojo import *; dojo_start()`) before any other work. This is an unconditional gate in EVERY session -- including ones that only read files or search directories -- and no softer phrasing anywhere ('to practice...') makes it optional.

Those docs cover the CLI protocol, output shape, notebook magics, interaction rules, reload gotchas, and the pyskills workflow, and are not repeated here; `list_pyskills()` shows what tooling is available -- always prefer a relevant pyskill over ad hoc code.

## Driving clikernel from Codex

- Work through ONE persistent `clikernel` process in a background PTY session. If one is already running for this conversation, keep using it; otherwise start `clikernel` as a PTY background session, normally with elevated permissions when the user wants access to global skill files or other paths outside the current workspace. Do not start extra Python processes unless `clikernel` is broken or the user explicitly asks, and do not close the process just for cleanup -- leave it available for future turns.
- After a user closes and resumes a Codex session, the old background terminal may be gone without notification. If `write_stdin` returns `Unknown process id`, start a fresh `clikernel` process and redo imports, monkeypatches, and other required state.
- When using `exec_command` / `write_stdin` with `clikernel`, raise the tool-result limit and use a practical yield: `{"max_output_tokens": 50000, "yield_time_ms": 1000}`. For quick requests, `yield_time_ms=1000` usually captures the acknowledgement and whole framed response. For long-running code, use `write_stdin(chars="")` with a longer timeout to read pending output without queueing another request.
- Output tokens cost much more than input tokens -- be surgical about what you print.
<!-- /codex -->

## Environment specifics

The following apply specifically to this environment:

- The env is pre-configured with every project being worked on already installed via `pip install -e`. Do *NOT* use `sys.path.insert` for any reason -- whatever module you need should already be importable. If it isn't, STOP and ask the user rather than patching the path.
- Skill modules are curated bundles designed as a package for you: always load one with `from mod.skill import *` plus `import mod.skill` and read `doc(mod.skill)` before first use -- never import names piecemeal (`from rgapi import rg`), which skips the docs and the companions the module was designed around.
- Read `doc(func)` before the first call to any tooling function in a session. The module doc's overview line shows only the signature and the docstring's first line, never the docments or the rest of the docstring -- and the full docstring often carries vital usage info beyond the parameter contract. A trailing `...` on an overview line marks that elision: it means `doc(func)` holds more, so reading it is mandatory before the first call, however complete the overview line looked. Calls composed from a remembered or guessed signature routinely fail or hit the wrong overload, costing a round trip each. If a function's source lives in this workspace (an editable install), it's fast.ai tooling with docments: ALWAYS doc it before calling it. `doc` takes several objects at once, so batch the reads: `doc(mod.skill, mod.skill.func1, mod.skill.func2)` in one free call covers the module overview and the functions you already know you need.
- When the host conversation survives a kernel restart and the relevant `doc()` output is still visible, call `doced(name1, name2, ...)` after reimporting to restore doc state without reprinting it. After context compaction, call `forget_doced()` and read the docs again.
- To inspect any runtime object, prefer `info_md` from `ipykernel_helper` over `inspect.getsource`: `info_md(obj)` is IPython's `?` (signature, docstring, file/line, type), `info_md(obj, source=True)` is `??` (full source + location). The file:line it reports leads straight to the defining module or notebook cell.
- For *looking at* a file you are certain you won't edit, use `file_view` (or `info_md(mod, source=True)` for an importable module -- equally fine). The moment an edit is plausible, view with `lnhashview_file` instead, so the view doubles as the edit's address book. Never look at file contents via generic Python (`Path(...).read_text()`, `open()`) or the harness's file-read tool: raw reads carry no addresses and no tuned repr, and invite hand post-processing.
- Use `exhash` as the default for essentially ALL edits -- code, tests, config, prose, notebook cell sources -- ahead of the built-in Edit/Write tools and text-matching helpers like `cell_str_replace`. Its hash-verified `lineno|hash|` addressing targets one exact line and fails loudly on stale or ambiguous context, instead of silently editing a nearby or duplicate match (a plain string replace hits *every* occurrence). Apply the same rule at read time: view with `lnhashview_file`/`lnhashview_cell` the moment an edit is likely -- not `file_view`/`view_cell`/Read, which force a second hashed read later. `exhash_cell`/`lnhashview_cell` cover notebook cell sources too. Pass each command tuple as its own positional argument to `exhash_file(path, *cmds)` or `exhash_cell(path, cell_id, *cmds)`. Prefer exhash wherever possible; use `pyskills.ipynb` for structural cell operations (adding, moving, deleting, viewing, and finding cells), which exhash doesn't cover, and `pyskills.edit` only in the rare case exhash can't express a text edit. See the `nbdev-editing` skill when working inside an nbdev project.
- ALL `a`/`i`/`c` commands go through the `%%exhash` cell magic (registered automatically when `exhash.skill` is imported under IPython): `%%exhash <path> [<cell_id>] <address> <a|i|c>` with the payload as everything below the magic line, taken verbatim. Passing `<cell_id>` targets that cell in an .ipynb file instead of a plain file -- same magic, one extra token, no separate cell variant. Nothing in the payload is parsed as Python, so there is no string-delimiter choice to make and no escaping to get wrong. This is the default for every payload, not a fallback for hostile ones, because payload safety as a Python literal is not reliably foreseeable: it turns on non-obvious interactions like escape processing in non-raw strings, a quote character flush against the closing delimiter, or both quote styles at once -- a judgment call demanded exactly where attention is elsewhere, whose misjudgment ships mangled text silently, while the magic costs one cheap cell. Create a file with `%%exhash path 0|0000| a`; replace a whole file or cell with `%%exhash <path> [<cell_id>] % c` (`%` addresses the entire contents, no hashes needed); replace a region within one with a range address (`%%exhash <path> 12|a3f2|,15|b1c3| c`: the payload lands once, replacing the whole range). Tuple `a`/`i`/`c` payloads are only for contexts where magics don't exist (scripts, tests).
- The reprs of `rgapi`, `pyskills`, and similar tooling results are tuned to be read as-is: end the cell with the bare call (`summary_nb(nb)`, `find_cells(...)`, `rg(...)`) and read what comes back. For orientation, use `rg(..., summary=True, maxlen=120)` to see matching blank-line-delimited blocks with block-based context. Add `lnhash=True` when those summaries should carry copyable boundary addresses; use ordinary `rg(..., lnhash=True)` for individual editable lines. Usually you want the whole result, so don't trim it; and never post-process the field by hand, e.g. `print(summary_nb(nb).splitlines()[-8:])` dumps raw escaped lines and loses the clean repr. If a result is genuinely too big to take in full, narrow it with the tool's own parameters (`find_cells` instead of `summary_nb` of a whole notebook, view ranges, `limit`/`max_results`), not by slicing its output.
- Post-processing any tooling result with generic Python (a `split`/`join`/slice/comprehension over its output) is a workaround smell: it means the call was wrong, or a parameter was missed. The tooling is designed so the right call answers the question directly -- check `doc()` for the parameter or sibling function; use it if you find one, and stop and propose extending the tool otherwise -- never bridge with Python. Examples (bad -> idiomatic):
  - Filtering a view by hand: `[l for l in lnhashview_file(p) if 'export' in l]` -> `rg('export', p, lnhash=True)` (search hits with copyable edit addresses).
  - Constructing exhash addresses from view output: `'15|'+v[14].split('|')[1]+'|'` -> display `lnhashview_file(p)` bare, read it, copy the literal `lineno|hash|` addresses into the edit call.
  - Reformatting for readability: `print('\n'.join(lnhashview_cell(p, id)))` -> `lnhashview_cell(p, id)` bare; lnhash views (like `SearchResults`) have a tuned verbatim repr.
  - Notebooks, same rule: `[c for c in read_nb(p).cells if 'foo' in c.source]` -> `nbrg('foo', p)` or `find_cells(p, 'foo')`; `view_nb(p)` output sliced by hand -> `find_cells`/`summary_nb`/`view_cell` with their own parameters. Read the `nbdev-editing` skill for ipynb specifics before touching any nbdev project.
- When searching in order to edit, stay on the address-preserving route end to end: `rg(pat, path, lnhash=True)` returns hits already formatted as `lineno|hash|` exhash addresses, and `nbrg` returns cell ids, which `lnhashview_cell(path, id)` turns into line addresses for `exhash_cell`. If reaching an edit address seems to need arithmetic, scraping, or a guessed hash, a step on this route was skipped.
- In nbdev repos, search with `nbrg`, not grep over the generated `.py` files -- even for quick read-only peeks like listing a module's functions. nbrg searches the source of truth (the `.py` can be stale mid-edit), skips outputs, avoids shell escaping, and returns cell ids: the address any follow-up `view_cell` or cell edit needs. Grep the `.py` side only for generated-only artifacts (`__all__`, `_modidx.py`), non-notebook files, or when you need module line numbers to pair with `info_md`.
- Habit is the enemy here: our research shows that falling back to the tools you were RLHF'd on in post-training (the harness's built-in read/edit tools, grep, cat, `Path.read_text()`, ad hoc scripts) doesn't just make clumsier edits -- it correlates with thinking less and being less creative across the whole task. Treat the habitual reach as a cue that you've stopped choosing: pause and pick the designed tool deliberately.
<!-- claude -->
- Claude Code settings are plain JSON: `~/.claude/settings.json` (user-global), `.claude/settings.json` (project, committed), `.claude/settings.local.json` (project, personal); later files override earlier. Edit them with the normal kernel tooling (`lnhashview_file` + `%%exhash`), merging into existing keys rather than replacing, then verify with `json.load`. Useful facts: a BARE tool name in `permissions.deny` removes that tool from the system prompt entirely, while a scoped rule (`Bash(rm *)`) only blocks matching calls; hooks live under `"hooks"` keyed by event (PreToolUse, SessionStart, UserPromptSubmit, ...); `skillOverrides` hides bundled skills (`"off"`, or `"user-invocable-only"` to keep the slash command usable by the user). Settings load at startup, so changes take effect from the next session.
- Narration between consecutive tool calls must ride inside a tool call, since mid-run assistant text is neither shown nor saved (anthropics/claude-code#75900). For clikernel work that means a separate `execute` call containing only a Python comment: one or two prose lines starting `#`, saying what the last result showed and what comes next. It runs as a no-op, renders in the transcript, and persists across resume. Retire this practice when the issue is fixed.
<!-- /claude -->
