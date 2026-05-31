from __future__ import annotations

import os
import sys
from pathlib import Path


def _repo_root(root_dir: str) -> Path:
    env_root = os.getenv("COCOGA_REPO_ROOT")
    if env_root:
        return Path(env_root).resolve()
    return Path(root_dir).resolve().parents[1]


if __name__ == "__main__":
    print("[*] Running ...")
    root_dir = sys.argv[2]
    mood = sys.argv[3]
    repo_root = _repo_root(root_dir)
    src_dir = repo_root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from cocoga.eval.llh_ga_operator import main_from_eval_script

    main_from_eval_script("tsp_ga_pair", "pair", root_dir, mood)
