# Frontend baseline audit

## Environment and limits

- Checkout: `/workspace/journal`.
- Branch: `work`; the pre-change working tree was clean.
- Quartz: 4.5.1 (`package.json` and installed package metadata).
- Runtime: Node v24.15.0 and npm 11.4.2.
- The clone is shallow and has no configured Git remotes or upstream-tracking refs. An exact
  comparison with upstream Quartz 4.5.1 is therefore deferred.
- `content_`, `content_generated`, `public`,
  `scripts/run_quartz_materialize_and_push.sh`, `tools/20_materialize_content.py`, and
  `tools/materialize_sessions.py` are absent from this checkout. This audit does not claim to
  verify the `content_generated -> content -> public` provenance or freshness contract.

## Initial checks

Before these changes, `npm run check` failed with unused-import errors for `truncate` in
`quartz.config.ts` and `FullSlug` in `quartz/components/Head.tsx`. `npm test` passed all 48
tests. `npm run build` failed because the package script invoked `quartz build`, but no
`quartz` executable was available on `PATH` for this self-hosted package.

## Confirmed findings and remediation

| Finding              | Root cause                                                                                                        | Change                                                                                                                      | Expected behavior                                                                                                            |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Vortex theme         | The vendored Obsidian Vortex bundle was imported by both `base.scss` and `custom.scss`.                           | Removed both imports, compensating Vortex/search rules, and the unused bundle.                                              | Quartz-native styles are the only active theme layer.                                                                        |
| Search modal         | Custom CSS changed the native fixed `.search-container` to `position: relative !important`.                       | Removed the broad `.search-container`, `.modal`, and `.autocomplete` override.                                              | Quartz owns fixed viewport Search geometry, focus, and stacking.                                                             |
| Explorer             | The layout rendered two mutually exclusive Explorers; a partial `stateKey` patch was emitted but never consumed.  | Restored one Explorer in each layout, explicitly hides only `tags`, and removed the unfinished `stateKey`/`data-key` patch. | Root-level and nested content are discoverable through one deterministic Explorer.                                           |
| Explorer persistence | `fileTree` JSON was parsed without validation.                                                                    | Added validated parsing with an empty-state fallback.                                                                       | Malformed saved state cannot stop Explorer initialization.                                                                   |
| Link transformation  | `CrawlLinks` ran twice with `absolute` and `shortest` strategies.                                                 | Retained one `absolute` transformer.                                                                                        | Relative Markdown links such as `../Business/note.md` are resolved once against the full path for folder and SPA navigation. |
| Baseline checks      | Two unrelated unused imports prevented type checking; the build script did not invoke the self-hosted Quartz CLI. | Removed unused imports and changed `build` to `./quartz/bootstrap-cli.mjs build`.                                           | Repository checks can run through the supported local Quartz CLI command.                                                    |

`Plugin.ContentIndex(...)` and `Component.Search()` remain configured. The single Explorer uses
one native `fileTree` local-storage key; `tags` is intentionally excluded from file navigation.

## Deferred work

- **Content provenance:** audit the absent materialization/promotion trees and generated output
  in an environment where they are present.
- **Professional visual pass:** add restrained design tokens only after browser-level functional
  checks are established.
- **Keywords/tags:** evaluate a dedicated tags/keywords component separately; it is not an
  Explorer concern in this baseline.
- **Upstream Quartz comparison:** fetch/configure an upstream Quartz 4.5.1 ref before declaring
  a complete modified-core diff.
- **Major-version migration:** no Quartz major-version migration is recommended or included in
  this stabilization task.

## Post-change verification

- `npm test` passed: 48 tests, 0 failures.
- `npm run build` completed using the local `./quartz/bootstrap-cli.mjs build` command. It found
  3,210 input files and produced `public/static/contentIndex.json` with 2,882 entries.
- Targeted Prettier verification passed for every changed source and documentation file.
- `npm run check` still reports pre-existing formatting violations across the repository's
  generated/authored content corpus and `.github/workflows/deploy.yml`; it no longer reports the
  two pre-change unused-import type errors. The content corpus was intentionally not reformatted
  as part of this frontend stabilization.
- This checkout has no browser automation setup. Native Search/Explorer contracts were verified
  statically in the generated production output (single Explorer per page layout, one
  `CrawlLinks` transformer, fixed native Search modal, and content index). Interactive browser
  smoke verification remains manual follow-up work.

## Vanilla Quartz baseline and Search diagnosis

- With Vortex removed, the source no longer imports a third-party theme bundle; `custom.scss`
  contains only the Quartz base import. Site metadata, Quartz theme tokens, Search, Explorer, and
  the `ContentIndex` emitter remain configured.
- A clean local production build completed before serving. The generated index was available at
  `/static/contentIndex.json` and contained representative content, including root and nested
  pages.
- Search uses Quartz's native fixed `.search-container` rule. No custom rules target
  `.search-container`, `.search`, `.modal`, `.autocomplete`, search inputs, or result lists.
- The Search implementation registers the native Ctrl/Command+K and Ctrl/Command+Shift+K
  handlers, supports `#` tag queries, and removes its document keydown handler through Quartz's
  navigation cleanup. The Search button cleanup now uses the same named listener reference for
  registration and removal. Closing Search now clears its selected-result reference, and keyboard
  navigation returns to the search field at either end of the result list rather than retaining a
  stale result after a close or trapping focus at a boundary.
- No global tag-highlighting keydown listener or `stopImmediatePropagation` call was found in the
  Quartz/site source. Graph and Escape handlers remain the only other document-level keydown
  listeners.
- Browser-level confirmation of click targets, focus traversal, result navigation, Escape focus
  restoration, SPA navigation, console/network errors, and repeated open/close behavior is still
  required in an environment with a browser. It was not inferred from static inspection.

## Explorer/sidebar diagnosis

- The single Explorer deliberately excludes only the generated `tags` branch. Root content folders
  such as `Accounting`, `AI`, `Health`, and `JobMarket`, as well as their nested note pages, are
  retained by the explicit filter.
- Folder titles now use Quartz's `link` behavior: `Accounting` navigates to the generated folder
  page at `/Accounting/`, while the distinct tag page remains `/tags/Accounting`. The folder icon
  remains the expansion control. This removes the prior ambiguity where clicking the folder title
  only collapsed it and could make the folder page appear unavailable.
- Folder display names remain Quartz-native: if a folder has an `index.md`, its title is used; if
  not, the folder segment is shown. The current-page link uses the native `.active` Explorer
  styling.
- Explorer saved state uses one `fileTree` key for the single instance. Invalid JSON and invalid
  entry shapes fall back to the default state rather than hiding content or aborting navigation.
- Desktop, tablet, mobile, and SPA-navigation interaction still require browser verification;
  this environment cannot provide it.
