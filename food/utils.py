def count_nutrition(before, count, name):
    type_1 = ['kalsium', 'fosfor', 'besi', 'natrium', 'kalium', 'tembaga', 'seng', 'retinol', 'thiamin', 'riboflavin', 'niasin', 'vit_c']
    type_2 = ['b_kar', 'kar_total']
    data = before * (count/100)
    if name == 'energi':
        ret = "{} {}".format(data, 'kal')
    elif name in type_1:
        ret = "{} {}".format(data, 'mg')
    elif name in type_2:
        ret = "{} {}".format(data, 'mcg')
    else:
        ret = "{} {}".format(data, 'g')
    return ret