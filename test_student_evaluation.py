import unittest
from student import calculate_result
from storage import find_student, add_record, delete_record
from queries import rank_students


class TestStudentEvaluationSystem(unittest.TestCase):

    def test_calculate_result_pass(self):
        result = calculate_result([80, 70, 90], 100)
        self.assertEqual(result[0], 240)
        self.assertEqual(result[1], 300)
        self.assertEqual(result[2], 80.0)
        self.assertEqual(result[3], 8.0)
        self.assertEqual(result[4], "PASS")

    def test_calculate_result_fail(self):
        result = calculate_result([30, 80, 90], 100)
        self.assertEqual(result[4], "FAIL")

    def test_student_storage(self):
        students = []
        record = ["26MIM10155", "Sanjay Perwal", 80, 70, 90, 240, 300, 80.0, 8.0, "PASS"]

        add_record(students, record)
        self.assertEqual(find_student(students, "26MIM10155"), 0)

        delete_record(students, 0)
        self.assertEqual(find_student(students, "26MIM10155"), -1)

    def test_ranking(self):
        students = [
            ["1", "Student A", 80, 80, 80, 240, 300, 80, 8.0, "PASS"],
            ["2", "Student B", 90, 90, 90, 270, 300, 90, 9.0, "PASS"]
        ]

        ranked = rank_students(students)
        self.assertEqual(ranked[0][1], "Student B")
        self.assertEqual(ranked[1][1], "Student A")


if __name__ == "__main__":
    unittest.main()
