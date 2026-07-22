# Answer.AI Skill Plugins

Skills from Answer.AI for both Codex and Claude Code, built from shared sources so the two stay in sync.

## Plugins

`codex-aai` (Codex) and `claude-aai` (Claude Code) carry the same skills, built from shared sources:

- `persistent-python`: work in a persistent `clikernel` IPython session - the workbench for inspection, debugging, editing, and experiments, with the pyskills tool ecosystem.
- `coding-patterns`: fastai coding style and conventions, including the TDD red-green testing process.
- `nbdev-editing`: the nbdev workflow, where notebooks in `nbs/` are the source of truth.
- `write-prose`: write prose that doesn't read as AI slop.
- `codex-docs` (Codex) / `claude-code-docs` (Claude Code): answer questions about the tool's behavior and configuration from its official documentation; one shared source (`src/skills/docs/`) with per-tool names and URLs.

`safecmd` (Claude Code) is separate: hooks that auto-approve safe bash commands using [safecmd](https://github.com/AnswerDotAI/safecmd)'s allowlist validation, so routine commands stop prompting for permission.

## Install: Codex

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add answerdotai/skill-plugins
```

Then open `/plugins` in Codex, select `Answer.AI Skill Plugins`, and install `Codex AAI`.

Plugin-installed skills are namespaced by plugin. The persistent Python skill appears as `codex-aai:persistent-python`.

For a plain `persistent-python` skill name, install the skill directly:

```text
Use $skill-installer to install https://github.com/answerdotai/skill-plugins/tree/main/plugins/codex-aai/skills/persistent-python
```

Restart Codex after installing.

## Install: Claude Code

Add this repository as a plugin marketplace, then install either or both plugins:

```text
/plugin marketplace add answerdotai/skill-plugins
/plugin install claude-aai@answerdotai-skill-plugins
/plugin install safecmd@answerdotai-skill-plugins
```

Skills appear namespaced as `claude-aai:persistent-python` etc. Nothing further is needed: Claude reads a skill when its trigger applies, and `safecmd`'s hooks run on every Bash call automatically.

## Development

Each skill has ONE source, in `src/skills/<name>/SKILL.md`: a jinja2 template rendered once per tool with `tool` (`codex` or `claude`) and `name` (that tool's built skill name) in context. Shared text stays bare; tool-specific text goes in `{% if tool == 'codex' %}...{% else %}...{% endif %}` blocks or `{{ }}` substitutions. Tool-specific extras (e.g. `agents/openai.yaml` for Codex) live in `src/skills/<name>/<tool>/` and are copied verbatim.

Never edit the generated files under `plugins/*/skills/` - edit the source and rebuild:

```bash
./build.py          # regenerate the plugin skill trees, bumping changed plugins (--no-bump to skip)
./build.py --check  # exit nonzero if any generated file is stale (for CI)
```

Generated outputs are committed, since installs pull the repo as-is.

To ship a change: edit `src/`, run `./build.py` (it bumps the version of each plugin whose output changed; `--no-bump` to skip), and commit. Installed plugins are cached per version, so users only see changes after a version bump plus update/reinstall. For live local use of your own checkout, skip installing the skills plugin and symlink instead, e.g. `~/.claude/skills/persistent-python -> plugins/claude-aai/skills/persistent-python`: edits are then picked up on the next build, no reinstall needed.

For local marketplace testing from this checkout:

```bash
codex plugin marketplace add ~/git/skill-plugins
```

and in Claude Code:

```text
/plugin marketplace add ~/git/skill-plugins
```

Runtime state should not be committed. Keep generated local state under ignored `state/` directories.

## License

Apache-2.0.
