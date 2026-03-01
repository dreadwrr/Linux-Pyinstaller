import re
import csv
import importlib.util
from collections import defaultdict
from .configfunctions import find_install


def update_filter_csv(RECENT, csv_file, escaped_user, user_filter):

    hits_dict = defaultdict(int)

    # load csv
    try:
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                pattern, count = row
                hits_dict[pattern] = int(count)
    except FileNotFoundError:
        pass  # or create csv
        # filter

    patterns = user_filter

    for pattern_literal in patterns:
        pattern = pattern_literal.replace("{{user}}", escaped_user)
        regex = re.compile(pattern)

        count = sum(1 for line in RECENT if len(line) >= 2 and regex.search(line[1]))
        hits_dict[pattern_literal] += count

    # add patterns not matched to csv
    for pattern_literal in patterns:
        hits_dict.setdefault(pattern_literal, 0)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Entry", "Hits"])
        for pattern_literal in patterns:
            writer.writerow([pattern_literal, hits_dict.get(pattern_literal, 0)])
        # original doesnt add new items to flth.csv
        # for pattern, count in hits_dict.items():
        #     writer.writerow([pattern, count])
