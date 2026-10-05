#!/usr/bin/env python3
# SpaceBack — a JDAC product. Copyright (c) 2026 JDAC, LLC. All rights reserved.
# Personal use only, on the recipient's own folders/projects — not on others' projects
# or for service delivery without written authorization from JDAC, LLC. Do not alter,
# resell, sublicense, redistribute, or present as your own work.
# Jonathan Schafer / JDAC Consulting / JDAC.ai
# 3.9-compatible duplicate scanner: size-group then smart content hash.
import os, sys, json, hashlib, argparse

CHUNK = 64 * 1024
SMALL = 1024 * 1024  # full-hash threshold

def smart_hash(path, size):
    h = hashlib.md5()
    try:
        with open(path, "rb") as f:
            if size <= SMALL:
                for blk in iter(lambda: f.read(1024 * 1024), b""):
                    h.update(blk)
            else:
                head = f.read(CHUNK)
                f.seek(-CHUNK, os.SEEK_END)
                tail = f.read(CHUNK)
                h.update(head)
                h.update(tail)
                h.update(str(size).encode())
    except (OSError, IOError):
        return None
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    print("Phase 1: indexing...", flush=True)
    by_size = {}
    count = 0
    for dirpath, dirnames, filenames in os.walk(args.root):
        for name in filenames:
            if name == ".DS_Store" or name == ".localized":
                continue
            fp = os.path.join(dirpath, name)
            if os.path.islink(fp):
                continue
            try:
                st = os.stat(fp)
            except OSError:
                continue
            if st.st_size == 0:
                continue
            by_size.setdefault(st.st_size, []).append((fp, st.st_mtime))
            count += 1
    print("indexed %d files, %d distinct sizes" % (count, len(by_size)), flush=True)

    candidates = {s: fs for s, fs in by_size.items() if len(fs) > 1}
    total_cand = sum(len(fs) for fs in candidates.values())
    print("Phase 2: hashing %d candidates in %d size-groups" % (total_cand, len(candidates)), flush=True)

    groups = {}
    done = 0
    for size, files in candidates.items():
        for fp, mtime in files:
            hh = smart_hash(fp, size)
            done += 1
            if done % 100 == 0:
                print("hashed %d/%d" % (done, total_cand), flush=True)
            if hh is None:
                continue
            key = "%s_%d" % (hh, size)
            groups.setdefault(key, []).append({
                "path": fp,
                "size": size,
                "mtime": mtime,
                "name": os.path.basename(fp),
            })

    dupes = {k: v for k, v in groups.items() if len(v) > 1}
    with open(args.out, "w") as f:
        json.dump(dupes, f, indent=2)

    total_wasted = sum(g[0]["size"] * (len(g) - 1) for g in dupes.values())
    print("DONE: %d groups, wasted %.2f GB" % (len(dupes), total_wasted / 1e9), flush=True)

if __name__ == "__main__":
    main()
