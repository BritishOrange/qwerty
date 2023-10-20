from tkinter import END


def mark_substrings(s, text_field):
    text = text_field.get("1.0", END)
    indexes = find_substring(s, text)

    text_field.tag_delete("Substring here")
    for i in range(len(indexes)):
        text_field.tag_add("Substring here",
                           str(indexes[i][0]) + '.' + str(indexes[i][1]),
                           str(indexes[i][2]) + '.' + str(indexes[i][3] + 1))

    text_field.tag_config("Substring here", background="yellow")


def find_substring(s, text):
    res = []
    line1, line2 = 0, 0
    last_n = -1
    for i in range(len(text) - len(s)):
        if text[i] == '\n':
            line1 += 1
            last_n = i
        if text[i] == s[0]:
            start = i - last_n - 1
            k = 0
            line2 = line1
            end = start - 1
            for j in range(i, len(text)):
                if text[j] == '\n':
                    line2 += 1
                    end = -1
                    continue
                if text[j] != s[k]:
                    break
                end += 1
                k += 1

                if k >= len(s):
                    res.append((line1 + 1, start, line2 + 1, end))
                    break

    return res


def check_correct(entry, text_f):
    s = entry.get()
    if s != '':
        mark_substrings(s, text_f)
