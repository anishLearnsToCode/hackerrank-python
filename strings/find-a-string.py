# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:(i + len(sub_string))] == sub_string:
                count += 1
                i += len(sub_string) - 1

    return count


string = input()
sub_string = input()
print(count_substring(string,sub_string))
