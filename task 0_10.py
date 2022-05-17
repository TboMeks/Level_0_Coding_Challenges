def output_common(word_i, word_ii):
    common = "common letters: "

    temp_string_i = word_i.lower()
    temp_string_ii = word_ii.lower()

    for i in temp_string_ii:

        if(temp_string_i.count(i) > 0):
            if(i != ""):

                common += +", "

    common = common[:-2]
    return common


print((output_common("Heart", "Heat"))
