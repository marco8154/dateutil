# Instructions for AI agents

`dateutil` is a small project with very limited maintainer time. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before making changes; this file covers the
things agents most often get wrong.

## Before opening an issue or pull request

Search for existing work first, and include closed and merged items:

```bash
gh issue list --repo dateutil/dateutil --state all --search "<key words>"
gh pr list --repo dateutil/dateutil --state all --search "<key words>"
gh pr list --repo dateutil/dateutil --state all --search "<issue number>"
```

Try several phrasings: the same bug is often reported in terms of different
functions (e.g. `parse` vs. `parser.parser`) or different time zones.

- If an open pull request already addresses the problem, do not open another
  one. You may review or suggest improvements on the existing one, but only
  do so if you believe it would be meaningfully improved by your contributions.
- If a merged pull request addresses it, check whether the problem still
  happens on `master` before going further.
- If a closed pull request addresses it, read why it was closed so you do not
  repeat the same approach.
- If an issue already exists, comment there (only if you have new
  information) rather than opening a new one.

Before reporting a bug, confirm it reproduces on the current `master` branch.

## Issues

Follow the bug report guidance in [CONTRIBUTING.md](CONTRIBUTING.md): a
minimal, self-contained reproducer, the `dateutil` and Python versions, and
what happens versus what you expected. For new features, open an issue for
discussion before writing a pull request.

## Pull requests

- **Use the pull request template.** `gh pr create --body`, `--fill`, the REST
  API and MCP tools do not apply `.github/pull_request_template.md` for you.
  Read the template and fill it in; do not delete its sections or rewrite the
  checklist.
- **Only tick checklist items that are actually done.**
- **Tests.** Every change in behavior needs a test that fails without the fix.
  Test through the public API where possible.
- **Changelog.** Add a news fragment in `changelog.d/` named
  `<number>.<type>.rst`, where `<type>` is one of `feature`, `bugfix`, `doc`,
  `deprecations`, `data` or `misc` (see `[tool.towncrier]` in
  `pyproject.toml`). See the
  [changelog section of CONTRIBUTING.md](CONTRIBUTING.md#changelog) for the
  required wording, including the "Reported by" / "Fixed by" credits. Never
  invent an issue or PR number; if you do not have one yet, add the fragment
  after the PR is opened.
- **AUTHORS.md.** If the person you are working for is not already listed in
  [AUTHORS.md](AUTHORS.md), add them, in alphabetical order, in the form
  `- Name <email> (gh: @handle) **D**`. Ask them how they want their name and
  e-mail to appear (the e-mail is optional); do not guess or use details from
  git config without asking.
- Keep pull requests focused on one change. Do not include unrelated
  reformatting or refactoring.
- **AI attribution.** Do not add `Co-authored-by:` trailers for an AI tool,
    in commits or in the PR description. If the user prefers to credit the
    tool, they may use an `Assisted-by:` trailer instead, e.g.
    `Assisted-by: <agent name>:<model and version>`.

## IMPORTANT: How to write issues, PR descriptions and comments

The maintainers strongly prefer clear and concise communication. Avoid large
blocks of text and front-load communications with concise information about
what needs improvement, what the current behavior is and what you expect. For
large amounts of background information or appendices, please use a details
tag.

- A PR description is a few sentences on what changed and why, plus
  `Closes #N` for the issue it fixes. The diff already shows what changed, so
  do not summarize it file by file.
- Do not add filler sections such as "Summary", "Overview" or "Key takeaways"
  on top of the template; the template already has the sections we want.
- Do not state that tests, linting or type checks pass. CI reports that.
- Describe the change, not the process. No "I'll", "Let me" or narration of
  what the agent did or tried along the way.
- No emoji decoration and no "Generated with ..." advertisements.
- When replying to a review comment, answer the question that was asked, in
  as few words as it takes.

Additionally, please do not directly comment on the repo, file issues or make
non-draft PRs without human review.

## Code comments

- Match the comment density of the surrounding code. Most lines need no
  comment.
- Do not write comments that restate what the code does. Comment only on
  *why*, when the reason is not obvious from the code itself.
- Comments describe the code as it is now. Never describe the previous
  behavior, the bug that prompted the change, or code that only existed in
  intermediate versions of your change (e.g. "now uses X instead of Y",
  "fixed the off-by-one here"). That history belongs in the commit message
  or the PR description.

## Where and how to make changes

### `dateutil.rrule`

The goal with `rrule` is to be compliant with the iCalendar RFCs (2445, 5545 and
the others in that lineage that have updated the RRULE and related data
types). Please keep this in mind when evaluating bugs and potential changes
to the API.

### `dateutil.tz`

Most of what `dateutil.tz` does has now been supplanted by the `zoneinfo`
module and `datetime.timezone`. If looking for something to do, better to focus
on other modules, but changes and bugfixes are accepted here.

### `dateutil.parser`

For the most part, `dateutil.parser.parse` is frozen. We may accept
improvements which provably give identical behavior or improve the *clearly
specified contract* of the function. Most of the function's behavior is very
poorly specified, and so most parse changes will *not* be accepted.

`dateutil.parser.isoparse` has a much better-specified contract, so changes to
it do not have the same restrictions.

### Other modules

There are no special instructions for other modules.

## Running the tests

Run tests with `tox` and in isolated environments if possible.


## swarvex project "dateutil absichern" (fork only)

This section applies to agents working on swarvex tasks in the fork
`marco8154/dateutil`. It does not change upstream rules above.

- Every task serves a claim in `docs/claims.md`. Never claim more than a test
  shows.
- Property tests go in `tests/property/`, named `test_<module>_prop.py` or
  `test_<topic>_prop.py`. Shared strategies go in
  `tests/property/strategies_<topic>.py` (imported as `from strategies_iso
  import ...`; `tests/property/` has no `__init__.py`).
- The pipeline loads a fixed Hypothesis profile
  (`swarvex_tools/hypothesis_profile.py`: derandomized, no database). Pin every
  failing input you find with `@example(...)`.
- A finding is checked in as a test marked
  `@pytest.mark.xfail(strict=True, reason="<report file>")`, plus a report
  draft in `docs/reports/` (English). Never post to upstream; a human does.
- New code and tests are licensed Apache-2.0 and BSD-3-Clause, like upstream
  (`docs/decisions/0001-lizenz.md`).
- Only use dependencies from `requirements-dev.txt` and the standard library
  (`zoneinfo`, `datetime.fromisoformat` as oracles).
  `hypothesis` and `tzdata` are pinned in `swarvex_tools/constraints.txt`.
- Oracle tests comparing `dateutil.tz` with `zoneinfo` use the `tz_source`
  fixture from `tests/conftest.py`, so both read the same time zone data.
- Your sandbox has no network: do not search upstream issues or reproduce on
  upstream `master` yourself; the lead does both before a report is sent.
- Commit messages: no `Co-authored-by:` trailer for an AI tool; use
  `Assisted-by: <agent name>:<model and version>` if you credit one.
- Tasks and project docs are in German; code, test names and upstream reports
  in English.
