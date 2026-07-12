---
name: coding-patterns
description: Jeremy's coding style and conventions (fastai style guide + 3 decades of experience), used across ALL his projects. TRIGGER — read before the first tool call that reads, writes, or searches files: the patterns are needed to discuss and assess code that's read or found, not only to write it. Tasks that never touch the filesystem don't need it. Certainly BEFORE writing or editing any Python: a new file, a one-line change, a test, a refactor, anything. Don't skip because a change "looks trivial" or you're "just" fixing one line. Covers naming, layout, concision, imports, testing process (TDD red-green, pytest), docments, versioning, and the fastcore/fasthtml ecosystem preference.
---

# Coding Patterns

Based on the fastai style guide and Jeremy's 3 decades of coding experience, and used across all of his projects, not only fastai ones.

Use the fastcore/fasthtml ecosystem (fastcore, fasthtml, fastlite, ...) when picking libraries - these are Jeremy's own, editable-installed as siblings, and preferred over heavier third-party alternatives.

## Every Construct Must Earn Its Place

Readers assume everything present is necessary. When they see `str(x)` on something that's already a str, they stop and wonder what subtle thing it's guarding against; when the answer is "nothing", they paid for a mystery with no payoff. The same goes for defensive copies (`list(x)` that's never mutated), "just in case" try/excepts, redundant type coercions, and unused parameters. Before adding any construct, know why it's needed; if you can't say, leave it out. The cost doubles in nbdev projects, where tests are documentation.

The same applies to prose in code: almost never add comments (only when the code is truly unclear), and don't add type hints, docstrings, or boilerplate that pull no weight. Prefer concise, readable code over verbose "enterprise" style.

## Docments

Docments are trailing comments on function parameters that fastcore uses for documentation. A signature with docments (or any long signature) uses this layout: `(` stays on the def line, each parameter on its own line indented 4, and `):` alone on its own line at def indent:

```python
@delegates(start_kernel)
async def run_kernel(
    kernel_name='python3', # Kernelspec name to launch
    manager_cls=KernelManager, # Manager class, e.g. a subclass customizing launch
    **kwargs
):
```

NEVER remove docments when refactoring - they're essential documentation.

When `**kwargs` passes through to a known callee, decorate with `@delegates(callee)` so the signature shows the real options - and delegates REQUIRES the collector to be named `kwargs`, not `kw` etc. Skip the decorator when the callee's own signature is just `**kwargs` (nothing to delegate).

## Raw Strings

Write any non-trivial string literal as a raw string (`r"..."` / `r"""..."""`): regexes, payload text for tools, code or markup inside strings, anything multi-line or containing backslashes. In plain strings a stray `\n` or `\d` either errors or silently corrupts, and each miss costs a round trip to diagnose plus another to fix. Raw strings are WYSIWYG, so the first attempt matches what you meant. The `r` costs nothing when no escapes are present, so make it the default, not the exception.

## Style Checker (chkstyle)

Run `chkstyle {path}` to check fastai style (only include path if needed). But use judgment - chkstyle is a hint, not gospel.

## Config Patterns

Read from standard locations rather than duplicating config:

- GitHub release notes config: `.github/release.yml`
- Project config: `pyproject.toml` under `[tool.yourpkg]`
- Infer values when possible (e.g., package name from `[project].name`)
- Bundle data files inside the package and read them with `importlib.resources`

## Versioning: Bump After Release

Versions are bumped immediately *after* release, so the tree always carries the next release's version. Hence a sibling dep pin can be written before it ships (`foo>=<foo's local version>`), releasing means shipping what's there (no suffix machinery, no bump step to forget), and bumping is part of releasing - Jeremy's step, never part of a change.

## Project Layout

Prefer flat layout over src/:

```
myproject/
├── mypkg/
│   └── __init__.py
├── tests/
├── pyproject.toml
└── README.md
```

## Testing

- ALWAYS use TDD-style red-green testing: write the test FIRST, run it to see it fail, THEN fix the code, then run again to see it pass
- Prefer as few tests as possible: a single test that walks through many checks is more readable and faster than many small tests
- Always create real test files, never ad-hoc python commands - tests lock in behavior for future refactoring
- Assert the logic, not incidentals: check what the behavior guarantees, never byte-exact renderings, exact reprs, or field order. A test that compares a whole output string locks in formatting decisions that were never the point, and breaks when an unrelated formatter or environment changes (e.g. assert the content appears in a markdown display block, not the display's exact payload)
  - NEVER use tests to "lock in" behavior, unless that exact behavior really is a key part of the logic or contract that must always be true forever
- Use `pytest -q` (not `python -m pytest`, which prompts for permission); nbdev projects use `nbdev-test` (see the nbdev-editing skill)
- Don't run slow-marked tests until finishing a session, or after a change likely to directly impact them

## One-liner Patterns

```python
# Conditionals
if not x: return default
if x and y: do_thing()

# Try/except
try: return run("cmd").strip() or default
except Exception: return default

# Loops
for i in range(n): result[i] = 0
while len(items) < 3: items.append(0)
```

## Import Style

Combine imports on single lines:

```python
import os, re, sys, shutil
from pathlib import Path
from fastcore.utils import *
```

`from fastcore.utils import *` already provides `os`, `Path`, and much of the stdlib - don't re-import those alongside it.
