---
name: claude-code-docs
description: Use when answering questions about current Claude Code behavior, configuration, CLI features, hooks, skills, plugins, sessions, compaction, permissions, or other Claude Code-specific interfaces from official documentation.
---

# Claude Code Docs

1. Work in `clikernel`. Fetch `https://code.claude.com/docs/llms.txt` exactly with `httpx`, save its text to a variable, and display the whole variable. It is the table of contents agents are meant to inspect.
2. Choose the link whose title matches the question. Do not replace the requested URL with a similar page.
3. Fetch that linked Markdown page with `httpx` and save its text to another variable. Never fetch `llms-full.txt`; select the relevant page from `llms.txt` instead.
4. Check the Markdown page's `len()`. If it is at most 30,000 characters, display the whole page. If it is larger, do not display it: load the `toolslm.read_md` pyskill, parse the page variable, inspect `paths()`, and retrieve the relevant sections. Fetch shared sections separately when an event-specific section refers to them.
5. Use the official documentation for documented interfaces and normal day-to-day behavior. Claude Code ships no public source; when the docs do not answer the question, check the changelog and What's New pages for recent changes, and investigate observed behavior directly (settings files, `--help`, `/doctor`).
6. Base the answer on the strongest applicable evidence: documented contracts for public behavior, and direct observation for runtime behavior. Distinguish among them when it matters.
