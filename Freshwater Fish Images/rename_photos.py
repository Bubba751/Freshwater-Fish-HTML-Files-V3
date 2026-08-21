"""
CB's Tropical Aquarium - Fish Photo Renamer
=============================================
Renames the .jpg files already downloaded by fish_photo_downloader.py so the
filenames match your fish list EXACTLY (with spaces), instead of underscores.

HOW TO RUN:
1. Save this file in the SAME folder that contains your "photos" subfolder
   (e.g. C:\FishPhotos\rename_photos.py, alongside C:\FishPhotos\photos\)
2. Open Command Prompt, cd to that folder:
       cd C:\FishPhotos
3. Run it:
       python rename_photos.py
4. It will rename every matching file in "photos" and print what it changed.

Safe to re-run - already-renamed files are simply skipped.
"""

import os

FISH_LIST = [
    "Apisto Bebas",
    "Betta Crowntail (Male)",
    "Betta Halfmoon (Female)",
    "Betta Halfmoon (Male)",
    "Betta Plakat (Female)",
    "Betta Plakat (Male)",
    "Catfish Cory Black",
    "Shrimp Cherry",
    "Cichlid Acara Blue",
    "Cichlid Apistogramma (Blue Pair)",
    "Cichlid Apistogramma (Orange Flash Pair)",
    "Cichlid Apistogramma (Petras Pair)",
    "Cichlid Apistogramma (Red Double Pair)",
    "Cichlid Apistogramma (Red Fire Pair)",
    "Cichlid Apistogramma (Red Super Pair)",
    "Cichlid Arowana (Small)",
    "Cichlid Arowana Jardini (Small)",
    "Cichlid Electric Blue Dempsey (Large)",
    "Cichlid Electric Blue Dempsey (Small)",
    "Cichlid Mbuna (Large)",
    "Cichlid Parrot Blood (Large)",
    "Cichlid Parrot Blood (Small)",
    "Cichlid Parrot Snow/Polar",
    "Cichlid Rainbow (Turquoise)",
    "Cichlid Severum Gold Red Spotted",
    "Cichlid Severum Spotted Gold",
    "Cichlid Silver Dollar",
    "Danio Glo",
    "Danio Zebra",
    "Discus Cobalt (Medium)",
    "Discus Discus (Large)",
    "Discus Discus (Small)",
    "Eel Peacock Eel (Small)",
    "Eel Tire Track Eel (Small)",
    "Eel Zig Zag Eel (Small)",
    "Frog African Dwarf",
    "Gourami Kissing",
    "Gourami Pearl (Large)",
    "Guppy (Female)",
    "Guppy (Male)",
    "Guppy Red Head Dumbo (Male)",
    "Guppy Red Head Tuxedo (Male)",
    "Guppy Red Tail Dumbo (Male)",
    "Loach Burma Border (Medium)",
    "Loach Clown (Large)",
    "Millenium Rainbow (Female)",
    "Millenium Rainbow (Male)",
    "Pleco L129",
    "Pleco LO18",
    "Pleco Longfin Red Bushynose",
    "Rainbow (Bosemani)",
    "Rainbow (Celebes)",
    "Rainbow (Dwarf Praycox)",
    "Rainbow (Emerald)",
    "Rainbow (Red)",
    "Red Crystal Shrimp",
    "Royal Farlowella",
    "Shrimp",
    "Shrimp Black Crystal",
    "Shrimp Yellow",
    "Singapore Shrimp",
    "Swordtail (Female)",
    "Swordtail (Male)",
    "Swordtail (Pair)",
    "Tetra Congo (Male)",
]

PHOTOS_DIR = "photos"


def old_filename(fish_name: str) -> str:
    # matches sanitize_filename() from the downloader script:
    # non [\w\s()-] chars stripped, then spaces -> underscores
    import re
    name = re.sub(r"[^\w\s()-]", "", fish_name)
    name = re.sub(r"\s+", "_", name.strip())
    return name + ".jpg"


def new_filename(fish_name: str) -> str:
    import re
    # keep the same character stripping, but preserve spaces
    name = re.sub(r"[^\w\s()/-]", "", fish_name)
    return name.strip() + ".jpg"


def main():
    if not os.path.isdir(PHOTOS_DIR):
        print(f'Could not find a "{PHOTOS_DIR}" folder next to this script.')
        return

    renamed, skipped, missing = 0, 0, []

    for fish in FISH_LIST:
        old_path = os.path.join(PHOTOS_DIR, old_filename(fish))
        new_path = os.path.join(PHOTOS_DIR, new_filename(fish))

        if os.path.exists(new_path):
            skipped += 1
            continue

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
            renamed += 1
        else:
            missing.append(fish)

    print(f"\nDone. Renamed {renamed}, already correct {skipped}, not found {len(missing)}.")
    if missing:
        print("\nCould not find a photo file for these (check REVIEW_NEEDED.txt):")
        for fish in missing:
            print(f"  - {fish}")


if __name__ == "__main__":
    main()
