import os
import subprocess

from tools.config import Config


def update_attack() -> None:
    """
    Download or update mitre source data.
    """
    if os.path.exists(Config.MITRE_ATTACK_DATA_PATH + "enterprise-attack"):
        subprocess.call(["git", "-C", Config.MITRE_ATTACK_DATA_PATH, "pull"], shell=False)
        return
    else:
        subprocess.call(["git", "clone", Config.ATTACK_URL, Config.MITRE_ATTACK_DATA_PATH], shell=False)
