while True:
    report = {}
    scores = []
    number = input("enter the number of students: ")
    if number.isnumeric() and number != "0":
        number = int(number)
        for student in range(1,number+1):
            print(f"=====student {student}====")
            while True:
                name = input(f"student name {student}: ")
                if name.replace(" ","").isalpha():
                    break
                else:
                    print("invalid name")
            while True:
                score = input(f"student core {student}: ")
                try:
                    score = float(score)
                    if 0 <= score <= 20:
                        scores.append(score)
                        if score < 10 :
                            status = "rejected"
                        elif 10 <= score < 15 :
                            status = "accepted"
                        elif 15 <= score < 18 :
                            status = "good"
                        else :
                            status = "excellent"

                        report[name] = {
                            "score" : score,
                            "status" : status
                        }
                        break
                    else:
                        print("invalid score (0-20)")
                except ValueError:
                    print("invalid score")
                    continue
                
        print("\n\n===final report===\n")
        for name , information in report.items():
            print(f"{name} : {information['score']} --> {information['status']}")
            
        print(f"\nnumber of student : {number}")
        total = 0
        for score in scores:
            total += score
        average = total / len(scores)
        
        print(f"average grades : {average}")
        print(f"highest score : {max(scores)}")
        print(f"lowest score : {min(scores)}\n")
        rejected_count = 0
        accepted_count = 0
        for info in report.values():
            if info['status'] == "rejected":
                rejected_count += 1
            else :
                accepted_count += 1
        print(f"number of successful : {accepted_count}")
        print(f"number of unsuccessful : {rejected_count}")
        exit()
    else:
        print("invalid number")