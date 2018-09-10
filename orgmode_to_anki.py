"""
Read in an org-mode and convert it to a tab-separated csv file suitable for use with Anki.
"""
from typing import List
import argparse


def read_orgmode_file(filename: str) -> List[str]:
    """
    Reads in an org-mode file and returns a list of strings, each containing a note.
    """
    notes = []
    try:
        with open(filename, 'r') as inputf:
            lines = inputf.readlines()
    except EnvironmentError as err:
        print('Problem occured while reading {}:'.format(filename), err)
    # Now convert the lines into notes
    current_line = ''
    for line in lines:
        # Org-mode notes start with "*"
        if current_line and line.startswith('*'):
            notes.append(current_line)
            current_line = line
        else:
            current_line += line
    return notes


def format_card(note: str) -> str:
    """Formats a single org-mode note as an HTML card."""
    lines = note.split('\n')
    if lines[0].startswith('* '):
        card_front = '<br />{}<br />'.format(lines[0][2:])
    else:
        print('Received an incorrectly formatted note: {}'.format(note))
        return ''
    card_back = '<br />'.join(lines[1:])
    return card_front + '\t' + card_back


def write_cards_to_file(cards: List[str], output_file: str, append: bool) -> None:
    """Write the list of cards to file."""
    if append:
        file_args = 'a'
    else:
        file_args = 'w'
    try:
        with open(output_file, file_args) as outputf:
            for card in cards:
                outputf.write(card + '\n')
    except EnvironmentError as err:
        print('Encountered issue while writing out file {}'.format(output_file), err)


def main() -> None:
    """Use read_orgmode_file() to read in a file, then operate on the resulting notes."""
    parser = argparse.ArgumentParser(description='Reads in an org-mode file and generates a ' +
                                     'matching YAML file for dnote.')
    parser.add_argument('-i', '--input', nargs=1, type=str, required=True, dest='input_file',
                        help='Location of the org-mode file to consume.')
    parser.add_argument('-o', '--output', nargs=1, type=str, required=True, dest='output_file',
                        help='Output file where YAML notes are written.')
    parser.add_argument('-a', '--append', action='store_true', help='Append to output file, ' +
                        'rather than writing to it.')
    args = parser.parse_args()
    input_file = args.input_file[0].strip()
    output_file = args.output_file[0].strip()
    notes = read_orgmode_file(input_file)
    cards = [format_card(note) for note in notes]
    write_cards_to_file(cards, output_file, args.append)


if __name__ == '__main__':
    main()