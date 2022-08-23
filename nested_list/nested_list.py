def second_best_grade(records):
    """Returns the grade that is second best in the class

    Args:
        records (List[list]): sublist in form [name,grade]

    Returns:
        float: Second Best grade on list
    """
    # put all grades in a set to remove duplicates
    # then convert to a list, so we can sort
    unique_grades = list({record[1] for record in records})
    unique_grades.sort()
    # get second grade in list
    return unique_grades[1]


def get_students_by_grade(records, target_grade):
    """Returns list of students with target grade alphabetical

    Args:
        target_grade (float): Grade that students must match
        records (List[list]): sublist in form [name,grade]

    Returns:
        List[str]: List of names sorted alphabetically

    """
    # filter only students with target grade
    matching_records = filter(lambda record: record[1] == target_grade, records)
    # list students names with that grade
    names = [record[0] for record in matching_records]
    names.sort()
    return names


if __name__ == "__main__":
    student_records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_records.append([name, score])

    answers = []
    second_best = second_best_grade(student_records)
    students = get_students_by_grade(student_records, second_best)
    for student in students:
        print(student)
