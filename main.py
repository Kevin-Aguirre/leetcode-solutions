#!/usr/bin/env python3

import usage
import sys
import lib

def main():
    if len(sys.argv) == 1:
        print(usage.mainUsageStr)
        return
    
    cmd = sys.argv[1]
    if (cmd == "add-problem"):
        if len(sys.argv) == 2: print(usage.add_problem_usage)
        elif (len(sys.argv) == 3): lib.handle_add_problem(sys.argv[2])
        else: print(f"Unrecgonized arguments for add-problem\n{usage.add_problem_usage}")
    elif (cmd == "rm-problem"):
        if len(sys.argv) != 3: print(usage.rm_problem_usage)
        lib.handle_rm_problem(sys.argv)
    elif (cmd == "sort-by-tag"):
        if len(sys.argv) < 3: print(usage.sort_by_tag_usage)
        lib.handle_sort_by_tag(sys.argv)
    elif (cmd == "top-topics"):
        lib.handle_top_topics(sys.argv)
    elif (cmd == "add-tags"):
        if len(sys.argv) < 3: print(usage.add_tags_usage)
        lib.handle_add_tags(sys.argv)
    else:
        print('unrecognized command')
        print(usage.mainUsageStr)
if __name__ == "__main__":
    main()