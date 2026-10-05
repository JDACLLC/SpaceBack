#!/usr/bin/env python3
import os, sys, shutil

DL = "/Users/jons/Downloads"
DRY = "--go" not in sys.argv

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
    for t in TARGETS:
        d = os.path.join(DL, t)
        if not DRY:
            os.makedirs(d, exist_ok=True)
    counts = {t:0 for t in TARGETS}
    moved = 0
    for name in os.listdir(DL):
        if name.startswith("."):
            continue
        if name in TARGETS:
            continue
        src = os.path.join(DL, name)
        is_dir = os.path.isdir(src) and not os.path.islink(src)
        dest_dir = classify(name, is_dir)
        counts[dest_dir] += 1
        dst = os.path.join(DL, dest_dir, name)
        if not DRY:
            if os.path.exists(dst):
                base, ext = os.path.splitext(name)
                k = 2
                while os.path.exists(os.path.join(DL, dest_dir, f"{base} ({k}){ext}")):
                    k += 1
                dst = os.path.join(DL, dest_dir, f"{base} ({k}){ext}")
            shutil.move(src, dst)
            moved += 1
    print("DRY RUN (no changes)" if DRY else f"MOVED {moved} items")
    for t in TARGETS:
        print(f"  {t:24} {counts[t]:5}")

if __name__ == "__main__":
    main()
