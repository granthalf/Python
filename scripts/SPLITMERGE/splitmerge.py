
#!/usr/bin/env python3

import argparse
import os
import sys
import glob


CHUNK_SIZE = 1024 * 1024  # 1 Mo


def split_file(input_file, num_parts):
    if num_parts < 1:
        raise ValueError("Number of parts need to be greater than zero.")

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Not found the file : {input_file}")

    file_size = os.path.getsize(input_file)
    base_size, remainder = divmod(file_size, num_parts)

    output_dir = os.path.dirname(os.path.abspath(input_file))
    filename = os.path.basename(input_file)

    with open(input_file, "rb") as source:
        for i in range(num_parts):
            part_size = base_size + (1 if i < remainder else 0)
            output_file = os.path.join(
                output_dir, f"{filename}.part{i + 1:03d}"
            )

            with open(output_file, "wb") as dest:
                remaining = part_size

                while remaining > 0:
                    chunk = source.read(min(CHUNK_SIZE, remaining))
                    if not chunk:
                        raise IOError("Can't full read the source file.")
                    dest.write(chunk)
                    remaining -= len(chunk)

            print(f"Created : {output_file} ({part_size} octets)")

    print(f"\nSplit achieved : {num_parts} parts.")


def merge_files(input_pattern, output_file):
    # Retrieve and sort the parts
    parts = sorted(glob.glob(input_pattern))

    if not parts:
        raise FileNotFoundError(
            f"Nopart found for : {input_pattern}"
        )

    # Avoid to include the out file with the parts
    output_abs = os.path.abspath(output_file)
    parts = [
        part for part in parts
        if os.path.abspath(part) != output_abs
    ]

    if not parts:
        raise ValueError("No validated part found.")

    with open(output_file, "wb") as dest:
        for part in parts:
            if not os.path.isfile(part):
                raise FileNotFoundError(f"Not found part : {part}")

            print(f"Add : {part}")

            with open(part, "rb") as source:
                while True:
                    chunk = source.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    dest.write(chunk)

    print(f"\nFile merged : {output_file}")
    print(f"Number of parts merged : {len(parts)}")
    print(f"Finale size : {os.path.getsize(output_file)} octets")


def main():
    parser = argparse.ArgumentParser(
        description=f"SPLIT: {os.path.basename(__file__)} split file nb_parts \n MERGE: {os.path.basename(__file__)} merge ''archive.zip.part*'' ''archive_out.zip'' \n [ Split or merge a file: {os.path.basename(__file__)} [-h] {{split,merge}} file [split_only:]{{nb_parts}} ]",
        usage="%(prog)s [-h] {split,merge} file [split_only:]{nb_parts} ..."
    )

    subparsers = parser.add_subparsers(
        dest="mode", required=True
    )

    # Mode split
    split_parser = subparsers.add_parser(
        "split", help="Split a file into N parts"
    )
    split_parser.add_argument("file", help="File to split")
    split_parser.add_argument(
        "parts", type=int, help="Number of parts"
    )

    # Mode merge
    merge_parser = subparsers.add_parser(
        "merge", help="Merge parts of a file"
    )
    merge_parser.add_argument(
        "pattern",
        help='Pattern of parts, as example "archive.zip.part*"'
    )
    merge_parser.add_argument(
        "output", help="Name of the merged file"
    )

    args = parser.parse_args()

    try:
        if args.mode == "split":
            split_file(args.file, args.parts)
        elif args.mode == "merge":
            merge_files(args.pattern, args.output)

    except (ValueError, FileNotFoundError, OSError) as exc:
        print(f"Error : {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
