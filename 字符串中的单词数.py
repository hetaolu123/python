def countSegments(s:str)-> int:
    segment_count = 0
    for i in range(len(s)):
        if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
            segment_count += 1
    return segment_count

s=input("请输入一段话，我会判断有几个单词：\n")
print(countSegments(s))