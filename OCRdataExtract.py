def get_x_and_y(data, word):
    index = 0
    for i in range(1, len(data)):
        if data[i]["description"] == word:
            index = i
            break

    seat_starting_x = data[index]["boundingPoly"]["vertices"][0]["x"]
    seat_starting_y = data[index]["boundingPoly"]["vertices"][0]["y"]
    data_2 = data[index+1:]
    return seat_starting_x, seat_starting_y, data_2, index


def get_seat_no_cords(data, x, y):
    x_cord = [i for i in range(x-20, x+20)]
    seat_no_cords = dict()
    for i in range(len(data)):
        if data[i]["boundingPoly"]["vertices"][0]["x"] in x_cord:
            seat_no_cords[data[i]["description"]] = [data[i]["boundingPoly"]
                                                     ["vertices"][0]["x"], data[i]["boundingPoly"]["vertices"][0]["y"]]

    seat_no_cord_with_index = dict()
    count = 0
    for key, val in seat_no_cords.items():
        temp = val.copy()
        temp.append(key)
        temp = list(dict.fromkeys(temp))
        seat_no_cord_with_index[count] = [temp]
        count += 1

    return seat_no_cord_with_index


def only_word(data, seat_no_cords):
    olny_names = list()
    for i in range(len(data)):
        if seat_no_cords[16][0][0] > data[i]["boundingPoly"]["vertices"][0]["x"]:
            olny_names.append(data[i])

    olny_names.sort(key=lambda x: x["boundingPoly"]["vertices"][0]["y"])
    return olny_names


def map_seat_no_with_names(seat_no_cords, olny_names):
    map_seat_no_with_name = dict()
    flag = 0
    c = 0
    st = ""
    name_li = list()
    name_with_cords = dict()
    y_start_end = list()
    for i in range(len(olny_names)):
        if c == 2:
            name_li.append(st)
            y_start_end.append(seat_no_cords[flag][0][2])
            name_with_cords[i] = y_start_end
            map_seat_no_with_name[seat_no_cords[flag][0][2]] = st
            y_start_end = list()
            st = ""
            c = 0
            flag += 1
        if olny_names[i]["boundingPoly"]["vertices"][0]["y"] >= seat_no_cords[flag][0][1] and olny_names[i]["boundingPoly"]["vertices"][0]["y"] <= seat_no_cords[flag+1][0][1]:
            if c == 0:
                st += olny_names[i]["description"]+" "
            if c == 1:
                st += olny_names[i]["description"]
            y_start_end.append(
                olny_names[i]["boundingPoly"]["vertices"][0]["y"])
            c += 1
    name_li.append(st)
    map_seat_no_with_name[seat_no_cords[flag][0][2]] = st

    return map_seat_no_with_name


def get_only_expected_words(data, start_x, start_y):
    only_mcq = list()
    start_x_ques_cord = [i for i in range(start_x-20, start_x+20)]

    for i in range(len(data)):
        if data[i]["boundingPoly"]["vertices"][0]["y"]-50 > start_y and data[i]["boundingPoly"]["vertices"][0]["x"] in start_x_ques_cord:
            only_mcq.append(data[i])

    return only_mcq


def map_seat_no_with_everything(data, to_be_mapped, seat_no_cords):
    seat_no_with_marks = dict()
    flag = 0
    for i in range(len(to_be_mapped)):
        if to_be_mapped[i]["boundingPoly"]["vertices"][0]["y"] >= seat_no_cords[flag][0][1] and to_be_mapped[i]["boundingPoly"]["vertices"][0]["y"] <= seat_no_cords[flag+1][0][1]:
            seat_no_with_marks[seat_no_cords[flag][0]
                               [2]] = to_be_mapped[i]["description"]
            flag += 1

    return seat_no_with_marks


def q2_q3_marks(only_descriptive):
    q_2_marks = list()
    q_3_marks = list()
    flag = 2
    for i in range(len(only_descriptive)):
        if i % 2 == 0:
            q_2_marks.append(only_descriptive[i]["description"])
        else:
            q_3_marks.append(only_descriptive[i]["description"])

    return q_2_marks, q_3_marks


def mapped_everything(map_seat_no_with_name_with_marks, mcq_marks, q_2_marks, q_3_marks):
    map_seat_no_with_name_with_marks_with_q2_q3 = dict()
    flag = 0
    for key, val in map_seat_no_with_name_with_marks.items():
        map_seat_no_with_name_with_marks_with_q2_q3[key] = [
            {
                "Name": map_seat_no_with_name_with_marks[key],
                "MCQ":mcq_marks[key],
                "Q2":q_2_marks[flag],
                "Q3":q_3_marks[flag]
            }]
        flag += 1

    return map_seat_no_with_name_with_marks_with_q2_q3


def over_all(data):
    x, y, d2, index_seat = get_x_and_y(data, "Seat")
    seat_no_cords = get_seat_no_cords(d2, x, y)
    x1, y1, data_name, index_student = get_x_and_y(data, "student")
    olny_names = only_word(data_name, seat_no_cords)
    map_seat_no_with_name = map_seat_no_with_names(seat_no_cords, olny_names)
    start_x, start_y, data_mcq, index_mcq = get_x_and_y(data, "MCQ")
    only_mcq = get_only_expected_words(data, start_x, start_y)
    only_mcq_seat = map_seat_no_with_everything(
        data, only_mcq, seat_no_cords)
    start_x, start_y, data_descriptive, index_descriptive = get_x_and_y(
        data, "Descripti")
    only_descriptive = get_only_expected_words(
        data_descriptive, start_x, start_y)
    q2_marks, q3_marks = q2_q3_marks(only_descriptive)
    final_data = mapped_everything(
        map_seat_no_with_name, only_mcq_seat, q2_marks, q3_marks)

    return final_data


if __name__ == "__main__":
    import json
    from pprint import pprint as pr
    with open('actual_res.json', encoding='utf-8') as f:
        data = json.load(f)
    data = data['textAnnotations']

    print(over_all(data))
