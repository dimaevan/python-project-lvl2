import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def generate_diff(file1, file2):
    current_directory = os.getcwd()
    example_path = os.path.join(current_directory, file1)
    compared_path = os.path.join(current_directory, file2)

    example = json.load(open(example_path))
    compared = json.load(open(compared_path))

    example_keys = set(example.keys())
    compared_keys = set(compared.keys())
    all_keys = sorted(example_keys.union(compared_keys))

    result = '{\n'
    for x in all_keys:
        if x in example_keys and x in compared_keys:
            if example[x] == compared[x]:
                result += beauty_result(x, example[x], ' ')
            else:
                result += beauty_result(x, example[x], '-')
                result += beauty_result(x, example[x], '+')
        elif x in example_keys:
            result += beauty_result(x, example[x], '-')
        elif x in compared_keys:
            result += beauty_result(x, compared[x], '+')
    result += '}'
    return result


def beauty_result(key, value, diff=" ", space='    '):
    return "{0}{1} {2}: {3} \n".format(space, diff + ' ', key, value)


if __name__ == '__main__':
    main()
