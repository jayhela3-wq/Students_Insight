CREATE TABLE students(
StudentID VARCHAR(20) PRIMARY KEY,
Name VARCHAR(100),
Gender VARCHAR(20),
Department VARCHAR(20),
AdmissionYear INT,
CurrentSemester INT,
Age INT
);

CREATE TABLE academic_performance(
StudentID VARCHAR(20),
Semester INT,
CGPA DECIMAL(4, 2),
MathScore DECIMAL(5, 2),
ProgrammingScore DECIMAL(5, 2),
DSAScore DECIMAL(5, 2),
ProjectScore DECIMAL(5, 2)
);

CREATE TABLE attendance(
StudentID VARCHAR(20),
Semester INT,
AttendancePercentage DECIMAL(5, 2)
);

CREATE TABLE skills(
StudentID VARCHAR(20) PRIMARY KEY,
PythonScore DECIMAL(5, 2),
JavaScore DECIMAL(5, 2),
DSAScore DECIMAL(5, 2),
MLScore DECIMAL(5, 2),
WebDevScore DECIMAL(5, 2),
CommunicationScore DECIMAL(5, 2)
);

CREATE TABLE placement(
StudentID VARCHAR(20) PRIMARY KEY,
AptitudeScore DECIMAL(5, 2),
InterviewScore DECIMAL(5, 2),
ResumeScore DECIMAL(5, 2),
InternshipCount INT,
HackathonCount INT,
PlacementStatus VARCHAR(20)
);

CREATE TABLE feedback(
FeedbackID VARCHAR(20) PRIMARY KEY,
StudentID VARCHAR(20),
FeedbackDate DATE,
Rating INT,
FeedbackText VARCHAR(500)
);


