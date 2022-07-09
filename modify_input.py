def modify_rows(rows,fields):
    modified_rows = []
    for row in rows:
        dummy = []
        for i in range(9):
            temp = []
            temp.append(row[0])  # append name
            temp.append(row[1])  # append username
            temp.append(row[2])  # append chapter tag
            temp.append(fields[3+6*i].split(" - ")[0])  # append testname
            temp.append(row[5+i*6])  # append answered
            temp.append(row[6+i*6])  # append correct
            temp.append(row[3+i*6])  # append score
            temp.append(row[8+i*6])  # append skipped
            temp.append(row[4+i*6])  # append time-taken
            temp.append(row[7+i*6])  # append wrong

            if '-' not in temp:
                dummy.append(temp)

        dummy.sort(key=lambda x: x[3])
        for i in dummy:
            modified_rows.append(i)
    return modified_rows