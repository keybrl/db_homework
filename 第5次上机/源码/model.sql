DROP TABLE IF EXISTS teach;
DROP TABLE IF EXISTS grade;
DROP TABLE IF EXISTS project_course;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS major;
DROP TABLE IF EXISTS department;


CREATE TABLE department (
  id VARCHAR(32) PRIMARY KEY NOT NULL,
  name VARCHAR(128) NOT NULL
);

CREATE TABLE major (
  id VARCHAR(32) PRIMARY KEY NOT NULL,
  dept_id VARCHAR(32),
  name VARCHAR(128) NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES department (id)
);

CREATE TABLE classes (
  id VARCHAR(32) PRIMARY KEY NOT NULL,
  major_id VARCHAR(32),
  grade_year YEAR,
  FOREIGN KEY (major_id) REFERENCES major (id)
);

CREATE TABLE student (
  id VARCHAR(32) PRIMARY KEY NOT NULL,
  class_id VARCHAR(32),
  name VARCHAR(128) NOT NULL,
  FOREIGN KEY (class_id) REFERENCES classes (id)
);

CREATE TABLE instructor (
  id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
  name VARCHAR(128)
);

CREATE TABLE course (
  id VARCHAR(32) PRIMARY KEY NOT NULL,
  name VARCHAR(128) NOT NULL,
  optional BOOLEAN DEFAULT FALSE NOT NULL,
  opt_credit NUMERIC(2, 1) DEFAULT 0 NOT NULL
);

CREATE TABLE project (
  id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
  major_id VARCHAR(32),
  grade_year YEAR,
  planning_year YEAR,
  opt_credit INTEGER,
  FOREIGN KEY (major_id) REFERENCES major (id)
);

CREATE TABLE project_course (
  project_id INTEGER,
  course_id VARCHAR(32),
  type INTEGER,
  credit NUMERIC(2, 1),
  PRIMARY KEY (project_id, course_id),
  FOREIGN KEY (project_id) REFERENCES project (id),
  FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE grade (
  student_id VARCHAR(32),
  course_id VARCHAR(32),
  score NUMERIC(4, 1),
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES student (id),
  FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE teach (
  class_id VARCHAR(32),
  instructor_id INTEGER,
  course_id VARCHAR(32),
  CONSTRAINT uni_class_instructor UNIQUE (class_id, instructor_id),
  PRIMARY KEY (class_id, instructor_id, course_id),
  FOREIGN KEY (class_id) REFERENCES classes (id),
  FOREIGN KEY (instructor_id) REFERENCES instructor (id),
  FOREIGN KEY (course_id) REFERENCES course (id)
);
