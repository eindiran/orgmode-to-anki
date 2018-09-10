# orgmode-to-anki
Convert an orgmode-formatted file into a format suitable for importing as Anki cards.

## Instructions
Run the `orgmode_to_anki.py` script over a `.org` file to produce a partially HTML formatted file suitable for use with Anki.

If your `.org` file is called `foo.org`, run the following command: `python3 orgmode_to_anki.py -i foo.org -o foo.txt`. This will produce a new file called `foo.txt`. You may then import the file into Anki using the standard import flow. Make sure that the field separating character is set to tab and that the "Allow HTML in fields" is checked.
