#!/usr/bin/env python3
# SpaceBack — a JDAC product. Copyright (c) 2026 JDAC, LLC. All rights reserved.
# Personal use only, on the recipient's own folders/projects — not on others' projects
# or for service delivery without written authorization from JDAC, LLC. Do not alter,
# resell, sublicense, redistribute, or present as your own work.
# Jonathan Schafer / JDAC Consulting / JDAC.ai
"""
SpaceBack organizer — sorts the top-level items of a folder into type folders.
Dry-run by default; pass --go to actually move. --root is REQUIRED (no default),
so the organizer can never run against the wrong folder.
"""
import os, sys, shutil, argparse

TARGETS = ["Images", "Videos", "Audio", "Documents",
           "Archives & Installers", "Projects & Folders"]

EXT = {
    "png":"Images","jpeg":"Images","jpg":"Images","heic":"Images","webp":"Images",
    "gif":"Images","svg":"Images","tiff":"Images","bmp":"Images",
    "mp4":"Videos","mov":"Videos","m4v":"Videos","avi":"Videos","mkv":"Videos","webm":"Videos",
    "m4a":"Audio","mp3":"Audio","wav":"Audio","aiff":"Audio","aac":"Audio",
    "pdf":"Documents","docx":"Documents","doc":"Documents","pptx":"Documents","ppt":"Documents",
    "xlsx":"Documents","xls":"Documents","csv":"Documents","tsv":"Documents","md":"Documents",
    "txt":"Documents","rtf":"Documents","html":"Documents","htm":"Documents","json":"Documents",
    "xml":"Documents","vtt":"Documents","srt":"Documents","vcf":"Documents","ics":"Documents",
    "key":"Documents","pages":"Documents","numbers":"Documents",
    "zip":"Archives & Installers","tgz":"Archives & Installers","gz":"Archives & Installers",
    "tar":"Archives & Installers","rar":"Archives & Installers","7z":"Archives & Installers",
    "dmg":"Archives & Installers","pkg":"Archives & Installers","app":"Archives & Installers",
}

def classify(name, is_dir):
    if is_dir:
        if name.lower().endswith(".app"):
            return "Archives & Installers"
        return "Projects & Folders"
    ext = name.rsplit(".",1)[-1].lower() if "." in name else ""
    return EXT.get(ext, "Documents")  # catch-all: loose unknown files -> Documents

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Folder to organize (required).")
    ap.add_argument("--go", action="store_true", help="Actually move (default is dry-run).")
    a = ap.parse_args()

    root = os.path.abspath(os.path.expanduser(a.root))
    dry = not a.go
    # Safety: must be an existing directory and not a filesystem/home root.
    if not os.path.isdir(root):
        sys.exit("error: --root is not a directory: %s" % root)
    if root in ("/", os.path.expanduser("~")):
        sys.exit("error: refusing to organize %s (too broad)" % root)

    for t in TARGETS:
        if not dry:
            os.makedirs(os.path.join(root, t), exist_ok=True)
    counts = {t: 0 for t in TARGETS}
    moved = 0
    for name in os.listdir(root):
        if name.startswith(".") or name in TARGETS:
            continue
        src = os.path.join(root, name)
        is_dir = os.path.isdir(src) and not os.path.islink(src)
        dest_dir = classify(name, is_dir)
        counts[dest_dir] += 1
        dst = os.path.join(root, dest_dir, name)
        if not dry:
            if os.path.exists(dst):
                base, ext = os.path.splitext(name)
                k = 2
                while os.path.exists(os.path.join(root, dest_dir, f"{base} ({k}){ext}")):
                    k += 1
                dst = os.path.join(root, dest_dir, f"{base} ({k}){ext}")
            shutil.move(src, dst)
            moved += 1
    print(("DRY RUN (no changes) — " if dry else "MOVED %d items — " % moved) + root)
    for t in TARGETS:
        print(f"  {t:24} {counts[t]:5}")

if __name__ == "__main__":
    main()
