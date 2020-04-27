from project.models import YzbUniversityName


def university_code_to_name():
    with open('E:\\web\\apps\\project\\utils\\university_code.txt', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")
            YzbUniversityName.objects.create(code=line[0], name=line[1])
