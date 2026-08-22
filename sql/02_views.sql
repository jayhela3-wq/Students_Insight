CREATE OR ALTER VIEW 
vw_student_performance AS
SELECT
s.StudentID,
s.Name,
s.Gender,
s.Department,
a.Semester,
a.CGPA,
a.MathScore,
a.ProgrammingScore,
a.DSAScore,
a.ProjectScore,
at.AttendancePercentage
FROM students s
JOIN academic_data a
ON s.StudentID = a.StudentID
JOIN attendance at
ON a.StudentID = at.StudentID
AND a.Semester = at.Semester;


SELECT COUNT(*) AS TotalRows
FROM vw_student_performance;

