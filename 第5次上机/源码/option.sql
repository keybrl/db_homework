# 1.	查询学生所选修的课程及成绩，并给出必修课平均成绩和选修课平均成绩；
# 查询成绩
SELECT
  student.id AS "Student ID",
  student.name AS "Student Name",
  course.id AS "Course ID",
  course.name AS "Course Name",
  grade.score AS "Score"
FROM
  grade
  JOIN student ON grade.student_id = student.id
  JOIN course ON grade.course_id = course.id
ORDER BY student_id, course_id;

# 计算平均成绩
SELECT *
FROM (
    SELECT grade.student_id AS "Student ID", student.name AS "Student Name", avg(grade.score) AS "Required Course Average Score"
    FROM grade JOIN student ON grade.student_id = student.id
    WHERE course_id IN (
      SELECT course_id
      FROM
        project_course JOIN
        project ON project_course.project_id = project.id JOIN
        classes ON project.major_id = classes.major_id JOIN
        student ON classes.id = student.class_id
      WHERE student.id = grade.student_id AND project_course.type = 1
    )
    GROUP BY student_id
    ORDER BY student_id
  ) req NATURAL JOIN (
    SELECT grade.student_id AS "Student ID", student.name AS "Student Name", avg(grade.score) AS "Selected Course Average Score"
    FROM grade JOIN student ON grade.student_id = student.id
    WHERE course_id IN (
      SELECT course_id
      FROM
        project_course JOIN
        project ON project_course.project_id = project.id JOIN
        classes ON project.major_id = classes.major_id JOIN
        student ON classes.id = student.class_id
      WHERE student.id = grade.student_id AND project_course.type = 2
    )
    GROUP BY student_id
    ORDER BY student_id
  ) sel NATURAL JOIN (
    SELECT grade.student_id AS "Student ID", student.name AS "Student Name", avg(grade.score) AS "Optional Course Average Score"
    FROM grade JOIN student ON grade.student_id = student.id
    WHERE course_id NOT IN (
      SELECT course_id
      FROM
        project_course JOIN
        project ON project_course.project_id = project.id JOIN
        classes ON project.major_id = classes.major_id JOIN
        student ON classes.id = student.class_id
      WHERE student.id = grade.student_id
    )
    GROUP BY student_id
    ORDER BY student_id
  ) opt;


# 2.	查某一个学生被哪些教师教过课；
# 假定其学号为“16130120191”
SELECT course.id AS "Course ID", course.name AS "Course Name", instructor.name AS "Instructor Name"
FROM
  project_course JOIN
  course ON course.id = project_course.course_id JOIN
  project ON project_course.project_id = project.id JOIN
  classes ON project.major_id = classes.major_id JOIN
  student ON classes.id = student.class_id JOIN
  teach ON classes.id = teach.class_id AND project_course.course_id = teach.course_id JOIN
  instructor ON instructor.id = teach.instructor_id
WHERE student.id = '16130120191';

# 3.	查询应被开除的学生（假定差2学分即被开除）。
SELECT fail_1.id, fail_1.name
FROM (
    SELECT student.id, student.name, sum(project_course.credit) AS fail_credit
    FROM
    project_course JOIN
    project ON project.id = project_course.project_id JOIN
    classes ON classes.major_id = project.major_id JOIN
    student ON classes.id = student.class_id JOIN
    grade ON project_course.course_id = grade.course_id AND project_course.type = 1 AND student.id = grade.student_id AND grade.score < 60
    GROUP BY project.id, student.id
  UNION (
    SELECT student.id, student.name, sum(project_course.credit) AS fail_credit
    FROM
      project_course JOIN
      project ON project.id = project_course.project_id JOIN
      classes ON classes.major_id = project.major_id JOIN
      student ON classes.id = student.class_id JOIN
      grade ON project_course.course_id = grade.course_id AND project_course.type = 1 AND student.id = grade.student_id AND grade.score < 60
    GROUP BY student.id
  ) UNION (
    SELECT grade.student_id AS "Student ID", student.name AS "Student Name", sum(course.opt_credit) AS fail_credit
    FROM grade JOIN student ON grade.student_id = student.id JOIN course ON course.id = grade.course_id
    WHERE course_id NOT IN (
      SELECT course_id
      FROM
        project_course JOIN
        project ON project_course.project_id = project.id JOIN
        classes ON project.major_id = classes.major_id JOIN
        student ON classes.id = student.class_id
      WHERE student.id = grade.student_id
    ) AND grade.score < 60
    GROUP BY student_id
    ORDER BY student_id
  )) fail_1
WHERE fail_credit > 2;
