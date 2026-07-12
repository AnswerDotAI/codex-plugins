---
name: codex-docs
description: Use when answering questions about current Codex behavior, configuration, CLI features, hooks, skills, plugins, sessions, compaction, permissions, or other Codex-specific interfaces from official documentation.
---

# Codex Docs

1. Work in `clikernel`. Fetch `https://learn.chatgpt.com/docs/llms.txt` exactly with `httpx`, save its text to a variable, and display the whole variable. It is the table of contents agents are meant to inspect.
2. Choose the link whose title matches the question. Do not replace the requested URL with a similar page.
3. Fetch that linked Markdown page with `httpx` and save its text to another variable. Never fetch `llms-full.txt`; select the relevant page from `llms.txt` instead.
4. Check the Markdown page's `len()`. If it is at most 30,000 characters, display the whole page. If it is larger, do not display it: load the `toolslm.read_md` pyskill, parse the page variable, inspect `paths()`, and retrieve the relevant sections. Fetch shared sections separately when an event-specific section refers to them.
5. Use the release documentation page as the behavior reference when it warns that linked `main` branch schemas may be newer than the installed release.
6. Base the answer on the selected official page and link it. Distinguish documented behavior from inference or observation.
