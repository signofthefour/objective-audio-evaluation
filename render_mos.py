#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment
import json
import os

WAVS_ROOT="bahnar_wavs/"
file_map=json.load(open(os.path.join(WAVS_ROOT, "file_map.json")))
file_text=json.load(open(os.path.join(WAVS_ROOT, "file_text.json")))
rawfile_map=json.load(open(os.path.join(WAVS_ROOT, "rawfile_map.json")))

genfiles_to_gt = {file_map[f]: f for f in file_map}
scratch_genfiles_to_gt = {rawfile_map[f] for f in rawfile_map}

choosen_files = list(file_map.values())[:3]
gt_files = list(file_map.keys())[:3]
wavs_folders=[f for f in os.listdir(WAVS_ROOT) if os.path.isdir(os.path.join(WAVS_ROOT,f)) and '.DS' not in f]
wavs_dict={f: [] for f in wavs_folders}

q_count = 1
folder_to_question = {f: [] for f in wavs_folders}
for f in wavs_dict:
    if f == 'GT':
        for file in gt_files:
            wavs_dict[f].append(
                {
                    "title": str(f"Question {q_count} : {str(file_text[file])}"),
                    "audio_path": os.path.join(WAVS_ROOT, 'GT', file),
                    "name": str(f"q{q_count}")
                }
            )
            folder_to_question[f].append(f"q{q_count}")
            q_count += 1
    elif 'scratch' in f:
        for gt_file in gt_files:
            wavs_dict[f].append(
                {
                    "title": str(f"Question {q_count}: {file_text[gt_file]}"),
                    "audio_path": str(os.path.join(WAVS_ROOT, f, rawfile_map[gt_file])),
                    "name": str(f"q{q_count}")
                }
            )
            folder_to_question[f].append(f"q{q_count}")
            q_count += 1
    else:
        for file in choosen_files:
            wavs_dict[f].append(
                {
                    "title": str(f"Question {q_count}: {file_text[genfiles_to_gt[file]]}"),
                    "audio_path": str(os.path.join(WAVS_ROOT, f, file)),
                    "name": str(f"q{q_count}")
                }
            )
            folder_to_question[f].append(f"q{q_count}")
            q_count += 1
    json.dump(folder_to_question, open('folder_to_questions.json', 'w+')) 
    
wavs_list = [wavs_dict[f] for f in wavs_dict]
from itertools import chain
wavs_list = list(chain(*wavs_list))
# print(wavs_list[0])

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS Evaluation",
        form_url="https://script.google.com/macros/s/AKfycbxMeOo_zd89wiFlGKmQf4xMyNgI97NRvgbxJFypTlWouUF7YGqXjIEp5jJziY3Thm6f/exec",
        form_id=1,
        questions=wavs_list
    )
    print(html)


if __name__ == "__main__":
    main()
