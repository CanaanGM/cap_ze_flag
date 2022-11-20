jumpled_message = "heT fl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"
#   'heT fl g a s i icp CTo {7F 4NR P05 1N5 _16 _35 P3X 51N 3_V 9AA B1F 8}7 '
#   'heT fl g a s i icp CTo {7F 4NR P05 1N5 _16 _35 P3X 51N 3_V 9AA B1F 8}7 '
#   'heT flga si pico CT F{7 R4N 5P0 51N 6_1 5_3 XP3 N51 V3_ A9A FB1 78}'
counter = 0
words = []
three_part_word = ""


for index, char in enumerate(jumpled_message):
    if len(three_part_word) == 3:
        words.append(three_part_word)
        three_part_word = ""
    elif char == "{" or char == "}":
        three_part_word += "*"
    else:
        three_part_word += char

print(words)
