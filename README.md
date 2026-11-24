# Fortune Cookie Wisdom for Developers

Entry for the make.fun competition
**u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44**
("Fortune Cookie Wisdom for Developers").

## The fortune

> You will fix the bug by deleting the code you were proudest of writing.

71 characters. One original fortune-cookie line for a software developer:
in true fortune-cookie voice ("You will..."), a single balanced sentence,
a truth every senior engineer recognises — the real fix is often deleting
code — turned in a way nobody has heard: the thing you must delete is the
code you loved most. On a second read, your proudest code *was* the bug.

## How it runs

`main.py` (Python 3.13, standard library only, no network at run time)
writes the line to `/output/entry.txt`, exactly, with no trailing newline.
It is fully deterministic: two runs produce byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — claim wallet for the entry
