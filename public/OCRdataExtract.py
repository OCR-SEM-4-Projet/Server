def get_x_and_y(data, word):
    for i in range(len(data)):
        if (data[i]['description'] == word):
            return data[i]['boundingPoly']['vertices'][0]['x'], data[i]['boundingPoly']['vertices'][0]['y']
    return 0, 0


def get_sorted_only_word(data, x, y, xLoffset=0, xRoffset=0, yTop=0, yBottom=0):
    only_stud_name_dict = list()
    for i in range(len(data)):
        if (data[i]['boundingPoly']['vertices'][0]['x'] >= x-xLoffset and data[i]['boundingPoly']['vertices'][0]['x'] <= x+xRoffset and data[i]['boundingPoly']['vertices'][0]['y'] >= y+yBottom):
            only_stud_name_dict.append(data[i])
    sorted_stud = sorted(
        only_stud_name_dict, key=lambda k: k['boundingPoly']['vertices'][0]['y'])
    return sorted_stud


def map_seat_number_with_name(sorted_seat_no, sorted_stud):
    map_seat_no_with_name = dict()
    flag = 0
    count = 0
    c = 0
    st = ""
    for i in range(36):
        try:
            if (sorted_seat_no[count]['boundingPoly']['vertices'][0]['y']-15 <= sorted_stud[flag]['boundingPoly']['vertices'][0]['y'] and sorted_stud[flag]['boundingPoly']['vertices'][0]['y'] <= sorted_seat_no[count+1]['boundingPoly']['vertices'][0]['y']):
                st += sorted_stud[flag]['description']+" "
                flag += 1
                c += 1
                if c == 2:
                    c = 0
                    map_seat_no_with_name[sorted_seat_no[count]
                                          ['description']] = st
                    count += 1
                    st = ""
                    continue
            else:
                count += 1
        except Exception as e:
            try:
                st += sorted_stud[flag]['description']+" "
                map_seat_no_with_name[sorted_seat_no[count]
                                      ['description']] = st
                flag += 1
            except Exception as e:
                break
            continue
    return map_seat_no_with_name


def map_seat_no_with_mcq_marks(sorted_seat_no, sorted_mcq_no):
    map_seat_no_with_mcq = dict()
    flag = 0
    count = 0
    for i in range(36):
        try:
            if (sorted_seat_no[count]['boundingPoly']['vertices'][0]['y']-15 <= sorted_mcq_no[flag]['boundingPoly']['vertices'][0]['y'] and sorted_mcq_no[flag]['boundingPoly']['vertices'][0]['y'] <= sorted_seat_no[count+1]['boundingPoly']['vertices'][0]['y']):
                map_seat_no_with_mcq[sorted_seat_no[count]
                                     ['description']] = sorted_mcq_no[flag]['description']
                flag += 1
            else:
                count += 1
        except Exception as e:
            try:
                map_seat_no_with_mcq[sorted_seat_no[count]
                                     ['description']] = sorted_mcq_no[flag]['description']
                flag += 1
            except Exception as e:
                break
            continue
    return map_seat_no_with_mcq


def q_2_and_q_3_marks(sorted_des_marks):
    q_2_marks = list()
    q_3_marks = list()
    flag = 2
    for i in range(len(sorted_des_marks)):
        if i % 2 == 0:
            q_2_marks.append(sorted_des_marks[i]["description"])
        else:
            q_3_marks.append(sorted_des_marks[i]["description"])

    return q_3_marks, q_2_marks


def map_everythings(map_seat_no_with_name, q_2_marks, q_3_marks, map_seat_no_with_mcq):
    map_everything = dict()
    count = 0
    for i in map_seat_no_with_name:
        try:
            map_everything[i] = [{
                "Name": map_seat_no_with_name[i], "MCQ": map_seat_no_with_mcq[i], "Q2": q_2_marks[count], "Q3": q_3_marks[count]}]
            count += 1
        except Exception as e:
            try:
                map_everything[i] = [{
                    "Name": map_seat_no_with_name[i], "MCQ": map_seat_no_with_mcq[i], "Q2": 0, "Q3": 0}]
            except Exception as e:
                try:
                    map_everything[i] = [{
                        "Name": map_seat_no_with_name[i], "MCQ": 0, "Q2": 0, "Q3": 0}]
                except Exception as e:
                    break
    return map_everything


def over_all(data):
    stud_x, stud_y = get_x_and_y(data, 'student')
    sorted_stud = get_sorted_only_word(
        data, stud_x, stud_y, xLoffset=120, xRoffset=70, yBottom=40)
    seat_x, seat_y = get_x_and_y(data, 'Seat')
    sorted_seat_no = get_sorted_only_word(
        data, seat_x, seat_y, xLoffset=50, xRoffset=50, yBottom=20)
    map_seat_no_with_name = map_seat_number_with_name(
        sorted_seat_no=sorted_seat_no, sorted_stud=sorted_stud)
    mcq_x, mcq_y = get_x_and_y(data, 'MCQ')
    sorted_mcq_no = get_sorted_only_word(
        data, mcq_x, mcq_y, xLoffset=40, xRoffset=10, yBottom=40)
    map_seat_no_with_mcq = map_seat_no_with_mcq_marks(
        sorted_seat_no=sorted_seat_no, sorted_mcq_no=sorted_mcq_no)
    des_x, des_y = get_x_and_y(data, 'Descripti')
    sorted_des_marks = get_sorted_only_word(
        data, des_x, des_y, xLoffset=10, xRoffset=20, yBottom=40)
    q_3_marks, q_2_marks = q_2_and_q_3_marks(sorted_des_marks)
    map_everything = map_everythings(
        map_seat_no_with_name=map_seat_no_with_name, q_2_marks=q_2_marks, q_3_marks=q_3_marks, map_seat_no_with_mcq=map_seat_no_with_mcq)
    return map_everything


if __name__ == '__main__':
    import json
    # from pprint import pprint as pp
    # load the json file
    with open('actual_res.json', encoding='utf-8') as f:
        data = json.load(f)

    data = data['textAnnotations']

    print("------------->>>> ")
    map_everything = over_all(data)
    print(map_everything)
