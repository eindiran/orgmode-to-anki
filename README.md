# orgmode-to-anki
Convert an orgmode-formatted file into a format suitable for importing as Anki cards. The file is tab-separated, using partial HTML formatting to specify newlines and more complex textually elements.

## Instructions
Run the `orgmode_to_anki.py` script over a `.org` file to produce a partially HTML formatted file suitable for use with Anki.

If your `.org` file is called `foo.org`, run the following command: `python3 orgmode_to_anki.py -i foo.org -o foo.txt`. This will produce a new file called `foo.txt`. You may then import the file into Anki using the standard import flow. Make sure that the field separating character is set to tab and that the "Allow HTML in fields" is checked.

Unless you are intending to update an existing deck, make sure you create a deck and point to it during the import process.

## Arguments
Find out more information about the available arguments by running `python3 orgmode_to_anki.py -h`. In addition to `-h` or `--help`, there are a few other flags:

* `-i` or `--input` specifies the `.org` file to use as a source.
* `-o` or `--output` specifies the location where the output file should be saved. A file type will not be added automatically.
* `-a` or `--append` sets that the output file should not be overwritten, but instead should be appended to. Given that Anki ignores duplicated cards by default, it shouldn't often be necessary to do this.

## Encoding
This script only works with UTF-8 (or ASCII) encoded text. If you have a `.org` file that is encoded in another encoding, the script will complain and fail to comlete running. Please convert it to UTF-8 using a tool like `iconv`.

For example, if you have a latin-1 encoded file:
`iconv -f iso-8859-1 -t utf-8 foo.org -o foo_utf8.org`
