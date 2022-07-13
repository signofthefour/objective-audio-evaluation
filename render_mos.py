#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment

filelist = 

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS Evaluation",
        form_url="https://script.google.com/macros/s/AKfycbyggDCaDEVXPh8Kk53zAfZr-moQB6KHnszpaQeUhQhkHYHCJ3l-DGBuVMph4VJnOUzUzQ/exec",
        form_id=1,
        questions=[
            {
                "title": "問題 1",
                "audio_path": "wavs/test1.wav",
                "name": "q1"
            },
            {
                "title": "問題 2",
                "audio_path": "wavs/test2.wav",
                "name": "q2"
            },
            {
                "title": "333",
                "audio_path": "wavs/test1.wav",
                "name": "q3"
            },
            {
                "title": "444",
                "audio_path": "wavs/test2.wav",
                "name": "q4"
            },
            {
                "title": "555",
                "audio_path": "wavs/test1.wav",
                "name": "q5"
            },
            {
                "title": "666",
                "audio_path": "wavs/test2.wav",
                "name": "q6"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
