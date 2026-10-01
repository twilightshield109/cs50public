import re
import sys


def main():
    print(parse(input("HTML: ")))

#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

def parse(s):
    pattern = r'src="(?:https?:\/\/)?(?:www\.)?(?:youtube\.com)\/(?:embed)\/([a-zA-Z0-9_-]+)?"'
    match = re.search(pattern,s)

    if re.search(r"<iframe (.+)>\<\/iframe>",s):
        if match:
            return (f"https://youtu.be/{match.group(1)}")
    else:
        return None

if __name__ == "__main__":
    main()
