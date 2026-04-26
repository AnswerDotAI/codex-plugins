# TODO

We are packaging the existing local `persistent-python` Codex skill as a shareable Codex plugin and direct-installable skill.

## Current State

- New local repo: `~/git/codex-plugins`
- Plugin/extension slug: `codex-aai`
- Marketplace file: `.agents/plugins/marketplace.json`
- Plugin source: `plugins/codex-aai/`
- Bundled skill: `plugins/codex-aai/skills/persistent-python/`
- Direct skill install path: `plugins/codex-aai/skills/persistent-python/`

## Done

- Created plugin scaffold for the original `persistent-python` package.
- Copied shareable skill files from `~/.codex/skills/persistent-python`:
  - `SKILL.md`
  - `agents/openai.yaml`
  - `scripts/clikernel_repl.sh`
- Excluded runtime `state/`.
- Added `.gitignore` with `tags` and `state/`.
- Added `README.md`.
- Added Apache-2.0 `LICENSE`.
- Set plugin manifest license to `Apache-2.0`.
- Fixed plugin copy of `SKILL.md`:
  - closed the broken code fence
  - changed the wrapper example to relative `scripts/clikernel_repl.sh`
- Validated before the rename:
  - plugin manifest parsed as JSON
  - `.agents/plugins/marketplace.json` parsed as JSON
  - bundled `persistent-python` skill passed `check_skill.py`
- Tested local marketplace install before the rename:
  - local marketplace add succeeded
  - `/plugins` install succeeded
  - a new session listed the plugin skill as `persistent-python:persistent-python`
  - the installed skill started `clikernel` and returned `42` for `6*7`
- Renamed the plugin/extension to `codex-aai` while keeping the bundled skill named `persistent-python`.
- Documented direct skill install via `$skill-installer` for users who want the plain `persistent-python` skill name.
- Validated after the `codex-aai` rename:
  - `plugins/codex-aai/.codex-plugin/plugin.json` parses as JSON
  - `.agents/plugins/marketplace.json` parses as JSON
  - `plugins/codex-aai/skills/persistent-python` passes `check_skill.py`

## Important Notes

- Plugin-installed skills are namespaced by plugin; after the rename, the expected plugin skill id is `codex-aai:persistent-python`.
- Direct skill install should expose the plain skill name `persistent-python`.
- Do not remove `agents/` to disable an old skill. `SKILL.md` is the discovery anchor; `agents/openai.yaml` is only metadata.
- Installing the plugin while a direct `persistent-python` skill is also installed may expose duplicate or near-duplicate persistent Python skills.
- Current public docs use `$HOME/.agents/skills` for direct skills. This machine also has active custom skills under `~/.codex/skills/` through `CODEX_HOME` behavior.

## Next Steps

1. Remove the previously installed local plugin/marketplace through the normal Codex plugin flow.
2. Add the local marketplace again and install `Codex AAI` from `/plugins`.
3. Verify a new session lists `codex-aai:persistent-python` and that the clikernel smoke test still works.
4. Commit and push.
5. Remove the local marketplace/plugin and test the GitHub marketplace install with:

   ```bash
   codex plugin marketplace add answerdotai/codex-plugins
   ```

6. Review whether plugin metadata and marketplace metadata are ready for first public use.

## Open Questions

- Should the plugin manifest include `author`, `homepage`, or legal URLs?
- Should we add assets/icons now or keep the first version text-only?
