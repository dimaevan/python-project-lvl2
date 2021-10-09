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
    keys = sorted(example_keys.union(compared_keys))

    result = '{\n'

    for key in keys:
        if key in example_keys:
            if key in compared_keys:
                if example[key] == compared[key]:
                    result += beauty_string(key, example[key], ' ')
                else:
                    result += beauty_string(key, example[key], '-')
                    result += beauty_string(key, compared[key], '+')
            else:
                result += beauty_string(key, example[key], '-')
        else:
            result += beauty_string(key, compared[key], '+')

    result += '}'
    return result


def beauty_string(key, value, diff=" ", space='    '):
    return "{0}{1} {2}: {3} \n".format(space, diff + ' ', key, value)


if __name__ == '__main__':
    main()
