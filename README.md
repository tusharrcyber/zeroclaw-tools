# ⚠️ Responsible Disclosure — Do NOT Install or Use

This repository is a **benign proof-of-claim** registered as part
of a responsible security disclosure to **Swisscom Bug Bounty**.

---

## Vulnerability: Dependency Confusion — Unclaimed PyPI Namespace

**Affected Repo:** https://github.com/swisscom/zeroclaw
**Package:** `zeroclaw-tools`
**Reported by:** cybertushar
**HackerOne:** https://hackerone.com/cybertushar
**Date:** September 2026
**Program:** Swisscom Bug Bounty
**Portal:** https://portal.bugbounty.swisscom.ch/
**Severity:** High — CVSS 3.1: 7.5

---

## What Was Found

Official Swisscom documentation instructs developers to run:

pip install zeroclaw-tools


This instruction appears across **8 files** in the official repo —
but the package **did not exist on PyPI** at time of research
(2026-09-07). Any attacker registering this name achieves **RCE**
on developer machines following official Swisscom docs.

**Affected files:**
- `docs/contributing/langgraph-integration.md`
- `docs/i18n/zh-CN/contributing/langgraph-integration.zh-CN.md`
- `docs/vi/langgraph-integration.md`
- `python/README.md` (2 references)
- `python/README.vi.md` (2 references)
- `python/zeroclaw_tools/integrations/discord_bot.py`

**Introducing commit:**

0b9a975d 2026-03-09 docs: restructure docs/ into topic-based directory layout


---

## Proof of Concept

- `poc_setup.py` — benign demo of attacker install hook
- PyPI placeholder: https://pypi.org/project/zeroclaw-tools/0.0.2/

---

## NO malicious code has been placed anywhere.

This repository and PyPI package exist solely to document the
vulnerability and prevent exploitation during responsible disclosure.
Ownership transferable to Swisscom on request.
