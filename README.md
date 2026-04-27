# Answer.AI Codex Plugins

Codex plugins and skills from Answer.AI.

## Plugins

- `codex-aai`: bundles Answer.AI Codex skills. It currently includes:
  - `persistent-python`: use a persistent `clikernel` Python workspace during a conversation.
  - `write-prose`: write human-sounding prose.

## Install Plugin

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add answerdotai/codex-plugins
```

Then open `/plugins` in Codex, select `Answer.AI Codex Plugins`, and install `Codex AAI`.

Plugin-installed skills are namespaced by plugin. The persistent Python skill appears as `codex-aai:persistent-python`.

## Direct Skill Install

For a plain `persistent-python` skill name, install the skill directly:

```text
Use $skill-installer to install https://github.com/answerdotai/codex-plugins/tree/main/plugins/codex-aai/skills/persistent-python
```

Restart Codex after installing.

## Development

For local marketplace testing from this checkout:

```bash
codex plugin marketplace add ~/git/codex-plugins
```

The plugin source lives in:

```text
plugins/codex-aai/
```

The bundled skill lives in:

```text
plugins/codex-aai/skills/persistent-python/
```

Runtime state should not be committed. Keep generated local state under ignored `state/` directories.

## License

Apache-2.0.

