# Answer.AI Skill Plugins

Skills from Answer.AI for both Codex and Claude Code, built from shared sources so the two stay in sync.

## Plugins

- `codex-aai` (Codex): `persistent-python`, `coding-patterns`, `nbdev-editing`, `write-prose`, and `codex-docs`.
- `claude-aai` (Claude Code): the same skills except `codex-docs`.

The skills cover a persistent `clikernel` Python workspace for live inspection, debugging, and editing; fastai coding conventions; the nbdev notebook-as-source workflow; and human-sounding prose.

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

Add this repository as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add answerdotai/skill-plugins
/plugin install claude-aai
```

Skills appear namespaced as `claude-aai:persistent-python` etc.

## Development

Each skill has ONE source, in `src/skills/<name>/SKILL.md`. Regions wrapped in `<!-- codex -->...<!-- /codex -->` or `<!-- claude -->...<!-- /claude -->` (whole-line or inline) appear only in that tool's output; everything else is shared. Tool-specific extras (e.g. `agents/openai.yaml` for Codex) live in `src/skills/<name>/<tool>/` and are copied verbatim.

Never edit the generated files under `plugins/*/skills/` - edit the source and rebuild:

```bash
./build.py          # regenerate plugins/codex-aai/skills/ and plugins/claude-aai/skills/
./build.py --check  # exit nonzero if any generated file is stale (for CI)
pytest -q           # build machinery tests (also runs a build)
```

Generated outputs are committed, since installs pull the repo as-is.

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
