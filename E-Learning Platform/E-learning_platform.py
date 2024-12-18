from abc import ABC, abstractmethod

class Person(ABC):
    _id_counter = 1000
    persons_list = []

    def __init__(self, name, email):
        self._id = Person._generate_id()
        self._name = name
        self._email = email

    @staticmethod
    def _generate_id():
        Person._id_counter += 1
        return Person._id_counter

    @classmethod
    def count_persons(cls):
        return len(cls.persons_list)

    @classmethod
    def get_all_persons(cls):
        return cls.persons_list

    @abstractmethod
    def get_details(self):
        pass

    @staticmethod  
    def display_main_details(self):
        return f"{self._name}, \nEmail: {self._email} \nPhone Number: {self.p_num}"
    
    @staticmethod
    def display_address(self):
        return f"{self.barangay}, {self.municipal}, {self.city}, {self.country} \nZip Code:  {self.zip_code}"

class Student(Person):
    student_count = 0  # Class variable to track the number of students
    students_list = []

    def __init__(self, name, email):
        self._id = Student.student_count + 1
        self._name = name
        self._email = email
        Student.student_count += 1

    def add_grade(self, assignment, grade):
        self._grades[assignment] = grade

    def get_details(self):
        return f"Student ID: {self._id}, Name: {self._name}, Email: {self._email}"
    
    @staticmethod
    def display_student_info(self):
        return (f"Student ID: {self.stud_id}\n"
                f"Course: {self.course_taken}\n"
                f"Date Joined: {self.date_joined}\n"
                f"{super().display_info()}")
    
    @classmethod
    def count_students(cls):
        return len(cls.students_list)


    @classmethod
    def find_student_by_id(cls, stud_id):
        for student in cls.students_list:
            if student.stud_id == stud_id:
                return student
        return None
    
    @classmethod
    def list_all_students(cls):
        return [student.display_full_name() for student in cls.students_list]

    @staticmethod
    def calculate_years_enrolled(date_joined, current_year):
        return current_year - int(date_joined.split('-')[0]) 


class Instructor(Person):
    instructor_count = 0  # Class variable to track the number of instructors
    instructors_list = []

    def __init__(self, name, email):
        self._id = Instructor.instructor_count + 1
        self._name = name
        self._email = email
        Instructor.instructor_count += 1

    def get_details(self):
        return f"Instructor ID: {self._id}, Name: {self._name}, Email: {self._email}"
    

    @classmethod
    def display_instructor_info(cls):
        return [instructor.display_instructor_info() for instructor in cls.instructors_list]
        
    @classmethod
    def count_instructors(cls):
        return len(cls.instructors_list)

    @classmethod
    def find_instructor_by_name(cls, full_name):
        for instructor in cls.instructors_list:
            if instructor.get_full_name() == full_name:
                return instructor
        return None

    @classmethod
    def list_all_instructors(cls):
        return [instructor.get_full_name() for instructor in cls.instructors_list]

    @staticmethod
    def validate_email(email):
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
class Course:
    _id_counter = 1
    credit_hours = 0
    learning_outcomes = []
    learning_materials = []
    

    def __init__(self, name, schedule):
        self._id = Course._id_counter
        Course._id_counter += 1  
        self._name = name
        self._schedule = schedule
    

    def get_course_details(self):
        return f"Course ID: {self._id}, Name: {self._name}, Schedule: {self._schedule}"

    

class Schedule(Course):

    def __init__(self, day, time):
        self._day = day
        self._time = time
        self._assignments = []

    def __str__(self):
        return f"{self._day} at {self._time}"


class Assignment(Course):
    __id_counter = 1

    def __init__(self, title, description, due_date):
        self._id = Assignment.__id_counter
        Assignment.__id_counter += 1  
        self._title = title
        self._description = description
        self._due_date = due_date


    def get_assignment_details(self):
        return f"Assignment ID: {self._id}, Title: {self._title}, Description: {self._description}, Due: {self._due_date}"
    
    @classmethod
    def display_feedback(self):
        return f"Feedback for {self._title} (Student: {self.student_id}): {self.feedback_text}"
    
    def add_assignment(self, assignment):
        self._assignments.append(assignment)

    def list_assignments(self):
        return [assignment.get_details() for assignment in self._assignments]


class Enrollment:
    def __init__(self, student, course):
        self._student = student
        self._course = course

    def enroll(self):
        print(f"{self._student._id} has been enrolled in {self._course._name}.")

    def get_enrollment_info(self):
        return f"{self._student.get_details()} enrolled in {self._course.get_course_details()}"


class UserManager:
    def __init__(self, file_path=None):
        self.students = []
        self.instructors = []
        self.courses_managed = []
        self.status = "active"
        self.file_path = file_path  # Initialize file_path
        self.user_activity_logs = []  # Initialize user activity logs

    def load_records(self):
        if not self.file_path:
            print("File path not set.")
            return
        try:
            with open(self.file_path, 'r') as file:
                self.records = file.read()
                print("Records loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_student(self, name, email):
        student_id = len(self.students) + 1  # Generate a simple ID
        student = Student(name, email)
        student._id = student_id 
        self.students.append(student)
        
        return f"Added student: {student._name}"

    def add_instructor(self, name, email):
        instructor_id = len(self.instructors) + 1  # Generate a simple ID
        instructor = Instructor(name, email)
        instructor._id = instructor_id
        self.instructors.append(instructor)
        
        return f"Added instructor: {instructor._name}"


    def delete_student(self, student_id):
        for student in self.students:
            if student._id == student_id:
                self.students.remove(student)
                print(f"Deleted student {student._name}")
                student_found = True
                break

        if student_found:
            # Update students.txt
            with open('students.txt', 'r') as file:
                lines = file.readlines()
            
            with open('students.txt', 'w') as file:
                for line in lines:
                    if not line.startswith(f"{student_id},"):
                        file.write(line)
        else:
            print("Student not found.")

    def delete_instructor(self, instructor_id):
        instructor_found = False
        for instructor in self.instructors:
            if instructor._id == instructor_id:
                self.instructors.remove(instructor)
                print(f"Deleted instructor {instructor._name}")
                instructor_found = True
                break

        if instructor_found:
            # Update instructors.txt
            with open('instructors.txt', 'r') as file:
                lines = file.readlines()
            
            with open('instructors.txt', 'w') as file:
                for line in lines:
                    if not line.startswith(f"{instructor_id},"):
                        file.write(line)
        else:
            print("Instructor not found.")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student._id == student_id:  
                return student
        return None

    def find_instructor_by_id(self, instructor_id):
        for instructor in self.instructors:
            if instructor._id == instructor_id:
                return instructor
        return None
    
    def list_students(self):
        return [student.get_details() for student in self.students]
    
    def list_instructors(self):
        return [instructor.get_details() for instructor in self.instructors]
    
    @staticmethod
    def log_activity(user, activity): 
        if user not in UserManager.user_activity_logs:  
            UserManager.user_activity_logs.append((user, activity))
            print(f"Logged activity for {user}: {activity}")

    def save_students_to_file(self):
        with open('students.txt', 'w') as file:
            for student in self.students:
                file.write(f"{student._id},{student._name},{student._email}\n")
        print("Students saved to file.")

    def save_instructors_to_file(self):
        with open('instructors.txt', 'w') as file:
            for instructor in self.instructors:
                file.write(f"{instructor._id},{instructor._name},{instructor._email}\n")
        print("Instructors saved to file.")


class CourseManager:
    def __init__(self):
        self.courses = []
        self.course_requests = []
        self.performance_reports = None
        self.course_reports = None
        self.assignments = []

    def add_course(self, course_name, day, time):
        schedule = Schedule(day, time)  
        course = Course(course_name, schedule)
        course_id = len(self.courses) + 1
        course._id = course_id
        self.courses.append(course)
        return course
    
    def add_assignments(self, title, description, due_date):
        assignment = Assignment(title, description, due_date)
        ass_id = len(self.assignments) + 1
        assignment._id = ass_id
        self.assignments.append(assignment)
        return assignment

    
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course._id == course_id:  
                return course
        return None

    def list_courses(self):
        return [course.get_course_details() for course in self.courses]
    
    def list_assignments(self):
        return [assignment.get_assignment_details() for assignment in self.assignments]

    def find_course_by_name(self, course_name):
        for course in self.courses:
            if course._name == course_name:
                return course
        return None

    def find_assignment_by_id(self, assignment_id):
            for ass in self.assignments:  # This line is incorrect
                if ass._id == assignment_id: 
                    return ass
            return None
    
    @classmethod 
    def increment_manager_count(cls): 
        cls.total_managers += 1

    @classmethod 
    def set_max_courses(cls, max_courses): 
        cls.max_courses = max_courses
    
    @classmethod 
    def get_total_managers(cls): 
        return
    @staticmethod 
    def validate_schedule(day, time): 
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
        return day in valid_days and isinstance(time, str)
    
    @staticmethod 
    def calculate_course_duration(start_date, end_date): 
        return (end_date - start_date).days
    
    def save_courses_to_file(self):
        with open('courses.txt', 'w') as file:
            for course in self.courses:
                file.write(f"{course._name},{course.schedule.day},{course.schedule.time}\n")
        print("Courses saved to file.")


class EnrollmentManager:
    total_enrollments = 0

    def __init__(self):
        self._enrollments = []

    def enroll(self, student, course):
        enrollment = Enrollment(student, course)
        self._enrollments.append(enrollment)
        EnrollmentManager.total_enrollments += 1

        with open('enrolledStudents.txt', 'a') as file:
            file.write(f"{student._id},{course._name}\n")
        print(f"Student ID: {student._id} successfully enrolled in {course._name}")

    def unenroll_student(self, student_id):
        enrollment_found = False
        with open('enrolledStudents.txt', 'r') as file:
            lines = file.readlines()

        with open('enrolledStudents.txt', 'w') as file:
            for line in lines:
                if not line.startswith(f"{student_id},"):
                    file.write(line)
                else:
                    enrollment_found = True

        if enrollment_found:
            print(f"Unenrolled student {student_id} from all courses")
        else:
            print(f"Enrollment not found for student {student_id}.")

    def view_enrolled_students(self):
        with open('enrolledStudents.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_id, course_name = line.strip().split(',')
                print(f"STUDENT ID: {student_id} COURSE: {course_name}")

    def list_enrollments(self):
        return [enrollment.get_enrollment_info() for enrollment in self._enrollments]
    
    @staticmethod
    def list_pending_enrollments(self): 
        return [enrollment.get_enrollment_info() for enrollment in self.pending_enrollments]
    
    @staticmethod
    def list_approved_enrollments(self): 
        return [enrollment.get_enrollment_info() for enrollment in self.approved_enrollments]
    
    @staticmethod
    def list_rejected_enrollments(self): 
        return [enrollment.get_enrollment_info() for enrollment in self.rejected_enrollments]

class GradeManager:
    overall_course_grades = 0
    overall_student_grade = 0

    def __init__(self):
        self.grades = {}  

    def add_grade(self, student, assignment, max_grade, score):
        if student._id not in self.grades:
            self.grades[student._id] = {}

        grade_percentage = (score / max_grade) * 100  
        self.grades[student._id][assignment._id] = {
            "score": score,
            "max_grade": max_grade,
            "percentage": grade_percentage,
            "status": "Passed" if grade_percentage >= 50 else "Failed"
        }
        with open('studentGrades.txt', 'a') as file: 
            file.write( f"{student._id},{assignment._id},{score},{max_grade},{grade_percentage:.2f},{self.grades[student._id][assignment._id]['status']}\n" ) 
        print(f"Grade added: {score}/{max_grade} ({grade_percentage:.2f}%)")

    def display_student_grades(self, student):
        grades_found = False
        print(f"\nGrades for {student._name}:")
        with open('studentGrades.txt', 'r') as file:
            for line in file:
                student_id, assignment_id, score, max_grade, percentage, status = line.strip().split(',')
                if int(student_id) == student._id:
                    print(
                        f"Assignment ID: {assignment_id}, "
                        f"Score: {score}/{max_grade}, "
                        f"Percentage: {percentage}%, Status: {status}"
                    )
                    grades_found = True
        
        if not grades_found:
            print(f"No grades available for {student._name}.")

class PlatformAdmin(UserManager, CourseManager, EnrollmentManager, GradeManager):
    def __init__(self, user_manager, course_manager, enrollment_manager, grade_manager):
        self.user_manager = user_manager
        self.course_manager = course_manager
        self.enrollment_manager = enrollment_manager
        self.grade_manager = grade_manager

    def add_sample_data(self, user_manager, course_manager):
        def sample_students():
            try:
                with open('students.txt', 'r') as file:
                    for line in file:
                        parts = line.strip().split(',')
                        if len(parts) == 3:
                            id, name, email = parts
                            student = Student(name, email)
                            student._id = int(id)  
                            self.user_manager.students.append(student)  
                        else:
                            print(f"Skipping line due to incorrect format: {line.strip()}")
            except FileNotFoundError:
                print("Students file not found.")

        def sample_instructors():
            try:
                with open('instructors.txt', 'r') as file:
                    for line in file:
                        id, name, email = line.strip().split(',')
                        instructor = Instructor(name, email)
                        instructor._id = int(id)  
                        user_manager.add_instructor(name, email)
            except FileNotFoundError:
                print("Instructors file not found.")

        def sample_courses():
            try:
                with open('courses.txt', 'r') as file:
                    for line in file:
                        name, day, time = line.strip().split(',')
                        course_manager.add_course(name, day, time)
            except FileNotFoundError:
                print("Courses file not found.")

        def sample_assignments():
            try:
                with open('assignments.txt', 'r') as file:
                    for line in file:
                        title, description, due_date = line.strip().split(',')
                        course_manager.add_assignments(title, description, due_date)
            except FileNotFoundError:
                print("Assignments file not found.")


        sample_students()
        sample_instructors()
        sample_courses()
        sample_assignments()

def main():
        user_manager = UserManager()
        course_manager = CourseManager()
        enrollment_manager = EnrollmentManager()
        grade_manager = GradeManager()
        platform_admin = PlatformAdmin(user_manager, course_manager, enrollment_manager, grade_manager)
        platform_admin.add_sample_data(user_manager, course_manager)

        while True:
            print("\n===== E-Learning Platform =====")
            
            print("\n--- ADD MENU ---")
            print("1. Add User (Student or Instructor)")
            print("2. Add Course")
            print("3. Add Assignment to Course")
            print("4. List All Users")
            print("5. List All Courses")
            
            print("\n--- GRADE SYSTEM ---")
            print("6. Add Grade")
            print("7. Display Student Grades")
            print("8. List All Assignments")
            
            print("\n--- ENROLLMENT ---")
            print("9. Enroll Student")
            print("10. Unenroll Student")
            print("11. View Enrolled Students in a Course")

            print("\n--- OTHER OPTIONS ---")
            print("12. Delete User (Student/Instructor)")
            print("13. Quit")
            
            print("\n===============================")
            
            choice = input("Enter your choice: ").strip()



            if choice == "1":
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                id_num = input("Enter ID number: ").strip()
                user_type = input("Add a Student or Instructor? (student/instructor): ").strip().lower()

                if user_type == "student":
                    result = user_manager.add_student(name, email)
                    with open('students.txt', 'a') as file:
                        student_id = id_num
                        file.write(f"{student_id},{name},{email}\n")
                    print(result)
                elif user_type == "instructor":
                    result = user_manager.add_instructor(name, email)
                    with open('instructors.txt', 'a') as file:
                        instructor_id = id_num
                        file.write(f"{instructor_id},{name},{email}\n")
                    print(result)
                else:
                    print("Invalid user type. Please enter 'student' or 'instructor'.")
            elif choice == "2":
                name = input("Enter course name: ").strip()
                day = input("Enter schedule day (e.g., Monday): ").strip()
                time = input("Enter schedule time (e.g., 9:00 AM): ").strip()
                result = course_manager.add_course(name, day, time)
                with open('courses.txt', 'a') as file:
                    file.write(f"{name},{day},{time}\n")
                print(result)

            elif choice == "3":
                course_name = input("Enter course name to add an assignment to: ").strip()
                course = course_manager.find_course_by_name(course_name)

                if course:
                    title = input("Enter assignment title: ").strip()
                    description = input("Enter assignment description: ").strip()
                    due_date = input("Enter assignment due date (e.g., 2024-11-30): ").strip()

                    result = course_manager.add_assignments(title, description, due_date)
                    with open('assignments.txt', 'a') as file:
                        assignment_id = len(course_manager.assignments)
                        file.write(f"{assignment_id},{title},{description},{due_date}\n")
                    print(f"Added assignment: {result.get_assignment_details()}")
                else:
                    print("Course not found. Please try again.")

            elif choice == "4":
                print("\n--- Users ---")
                users = user_manager.list_students()
                for user in users:
                    print(user) 

                instructors = user_manager.list_instructors()
                for ins in instructors:
                    print(ins)  


            elif choice == "5":
                print("\n--- Courses ---")
                courses = course_manager.list_courses()
                for course in courses:
                    print(course)

            elif choice == "6":
                student_id = int(input("Enter student ID: ").strip())
                assignment_id = int(input("Enter assignment ID: ").strip())
                max_grade = float(input("Enter maximum grade: ").strip())
                score = float(input("Enter student's score: ").strip())

                student = user_manager.find_student_by_id(student_id)
                assignment = course_manager.find_assignment_by_id(assignment_id)

                if student and assignment:
                    grade_manager.add_grade(student, assignment, max_grade, score)
                else:
                    print("Error: Student or assignment not found. Please try again.")

            elif choice == "7":
                student_id = int(input("Enter student ID to display grades: ").strip())
                student = user_manager.find_student_by_id(student_id)

                if student:
                    grade_manager.display_student_grades(student)
                else:
                    print("Error: Student not found. Please try again.")

            elif choice == "8":
                print("\n--- Assignments ---")
                assignments = course_manager.list_assignments()
                for assignment in assignments:
                    print(assignment)

            elif choice == "9":
                student_id = int(input("Enter student ID to enroll: ").strip())
                course_name = input("Enter course name to enroll the student in: ").strip()
                course = course_manager.find_course_by_name(course_name)
                student = user_manager.find_student_by_id(student_id)

                if student and course:
                    enrollment_manager.enroll(student, course)
                else:
                    print("Error: Student or course not found. Please try again.")

            elif choice == "10":
                student_id = int(input("Enter Student ID to unenroll: ").strip())
                student = user_manager.find_student_by_id(student_id)

                if student:
                    enrollment_manager.unenroll_student(student_id)
                else:
                    print("Error: Student not found. Please try again.")
                    
            elif choice == "11":
                enrollment_manager.view_enrolled_students()

            elif choice == "12":
                user_type = input("Delete a Student or Instructor? (student/instructor): ").strip().lower()
                user_id = int(input("Enter ID to delete: ").strip())

                if user_type == "student":
                    user_manager.delete_student(user_id)
                elif user_type == "instructor":
                    user_manager.delete_instructor(user_id)
                else:
                    print("Invalid user type. Please enter 'student' or 'instructor'.")

            elif choice == "13":
                print("Exiting the platform.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()