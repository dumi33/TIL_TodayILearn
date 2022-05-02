# 출석확인  
# /checks/attendance/<classIdx>
@blue_check.route("/attendance/<int:classIdx>",methods=['POST'])
def CreatesCheck(classIdx) :
    if request.method =='POST' :
        capture_addr = 'C:\\Users\\dumi3\\checkcmate_pro2\\CheckMate_Project\\capture_img.png'
        data = list(Class.find({"classIdx" : classIdx})) # 해당 클래스정보 
        student_img_addr = data[0]['studentImgAddr'] # 해당 클래스의 학생 이미지 경로
        # 학생들의 임베딩값 추출 & 출석확인
        students =Embedding.Create_Check(student_img_addr, capture_addr) # 출석한 학생의 레이블 
        print("출석한 학생은 {}입니다.".format(students))
        classStudentList=list(Student.find({"classIdx" : classIdx},{"_id" : 0, "name":1}))
        
        studentList = [] # 학생의 이름만을 추출 
        for i in range(len(classStudentList)) :
            studentList.append(classStudentList[i]['name'])
            
        noattendance = list(set(studentList) - set(students)) # 모든 학생 중 안온학생을 구함 
        print("출석하지 않은 학생은 {}입니다.".format(noattendance))
        
        x = dt.datetime.now()
        date = str(x.year)+"년 "+str(x.month)+"월 "+str(x.day) + "일"
        Attendance.update_one({"classIdx" : classIdx}, # 날짜와 출석하지 않은 학생 DB에 저장 
                {   "$set" :
                    {date : noattendance }
                }
            ) 
        
        return make_response(jsonify(SUCCESS=True),200)
