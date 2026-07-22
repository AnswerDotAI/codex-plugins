---
name: codex-docs
description: Use when answering questions about current Codex behavior, configuration, CLI features, hooks, skills, plugins, sessions, compaction, permissions, or other Codex-specific interfaces from official documentation.
---

# Codex Docs

1. Work in `clikernel`. Fetch `https://learn.chatgpt.com/docs/llms.txt` exactly with `httpx`, save its text to a variable, and display the whole variable. It is the table of contents agents are meant to inspect.
2. Choose the link whose title matches the question. Do not replace the requested URL with a similar page.
3. Fetch that linked Markdown page with `httpx` and save its text to another variable. Never fetch `llms-full.txt`; select the relevant page from `llms.txt` instead.
4. Check the Markdown page's `len()`. If it is at most 30,000 characters, display the whole page. If it is larger, do not display it: load the `toolslm.read_md` pyskill, parse the page variable, inspect `paths()`, and retrieve the relevant sections. Fetch shared sections separately when an event-specific section refers to them.
5. Use the official documentation for documented interfaces and normal day-to-day behavior. Dive into the Codex source when the docs do not answer the question, when implementation details matter, or when investigating observed behavior. Prefer source matching the installed build; if the source may be newer or older, say so.
6. Base the answer on the strongest applicable evidence: documented contracts for public behavior, matching source for implementation details, and direct observation for runtime behavior. Distinguish among them when it matters.
