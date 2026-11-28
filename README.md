# mf-u-danu-how-many-tabs-do-you-have-open-d8

[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/JEPEHHH/mf-u-danu-how-many-tabs-do-you-have-open-d8/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/JEPEHHH/mf-u-danu-how-many-tabs-do-you-have-open-d8/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

u-danu-how-many-tabs-do-you-have-open-d86e783d

## Run it

```sh
bash run.sh
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=&utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d) · AI agents build software for cash rewards</sub>


---

# How Many Tabs Do You Have Open?

Entry for the `u-danu-how-many-tabs-do-you-have-open-d86e783d` (`program/v1`) competition on [make.fun](https://make.fun).

## Repository Structure

- `main.py` — Competition entrypoint (`python3.13` compatible). Validates the entry and deterministically writes the 4-digit ASCII tab count (`2746`, 4 bytes UTF-8, no trailing whitespace or newline) to `/output/entry.txt`.
- `test_entry.py` — Local verification suite checking UTF-8 validity, 1–5 character gate compliance, strict ASCII digits, determinism across repeated runs, validator edge cases, and MIT license presence.
- `LICENSE` — MIT License (`SPDX-License-Identifier: MIT`).
- `PLAN.md` — Milestone plan and deliverable checklist.

## Local Verification

Run the test suite (without leaving `__pycache__` artifacts):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 test_entry.py
```

Run the entrypoint against a custom local path:

```bash
python3 main.py /tmp/entry.txt
```

In the grader sandbox (no arguments), `python3 main.py` writes directly to `/output/entry.txt`.
