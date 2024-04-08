class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        Greedy

        - no matter how many times we cycle, if theres a sandwich
        that a student wants, they will get it
        - so allocate each sandwich to each person no matter the 
        order they come in

        n is the length of students
        m is the length of sandwiches
        Time: O(m + n)
        Space: O(1)
        '''
        # count how many available of each sandwich
        circle_cnt = 0
        square_cnt = 0
        for student in students:
            if student == 0:
                circle_cnt += 1
            else:
                square_cnt += 1

        # allocate each sandwich
        for sandwich in sandwiches:
            if sandwich == 0:
                if circle_cnt == 0:
                    return square_cnt
                circle_cnt -= 1
            else:
                if square_cnt == 0:
                    return circle_cnt
                square_cnt -= 1

        return 0


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        Simulation

        n is the length of students
        m is the length of sandwiches
        Time: O(n^2)
        Space: O(n + m)
        '''
        # turn into a proper stack
        students = collections.deque(students)
        sandwiches = sandwiches[::-1]

        while sandwiches:
            starting_num_students = len(students)
            students_served = 0
            while students_served != len(students):

                first_in_line_student = students.popleft()
                # stop cycling through students if the current student
                # wants the sandwich
                if first_in_line_student == sandwiches[-1]:
                    sandwiches.pop()
                    break

                students.append(first_in_line_student)
                students_served += 1

            # if no students took the sandwich on one cycle,
            # stop the loop
            if students_served == starting_num_students:
                break

        return len(sandwiches)
