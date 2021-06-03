type_1 = ['kalsium', 'fosfor', 'besi', 'natrium', 'kalium', 'tembaga', 'seng', 'retinol', 'thiamin', 'riboflavin',
          'niasin', 'vit_c']
type_2 = ['b_kar', 'kar_total']


def count_nutrition(before, count, name):

    data = round(before * (count/100))
    if name == 'energi':
        ret = "{} {}".format(data, 'kal')
    elif name in type_1:
        ret = "{} {}".format(data, 'mg')
    elif name in type_2:
        ret = "{} {}".format(data, 'mcg')
    else:
        ret = "{} {}".format(data, 'g')
    return ret


def convert_mg_to_g(name, nutrition):
    if name in type_1:
        nutri = round(float(nutrition) / 1000)
        return nutri
    else:
        return float(nutrition)


def count_presentation(nutrition, total):
    presentation = round((nutrition / total) * 100)
    return presentation