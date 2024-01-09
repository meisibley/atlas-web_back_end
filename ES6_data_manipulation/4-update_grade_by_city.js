export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsLocat = students.filter((item) => item.location === city);

  // initial all students of the city grades to N/A
  for (const elem of studentsLocat) {
    elem.grade = 'N/A';
  }
  const studentsUpdateGrades = studentsLocat.map((items) => {
    for (const nGrade of newGrades) {
      // if the student's id is in newGrade, update whose grade
      if (items.id === nGrade.studentId) {
        items.grade = nGrade.grade;
      }
    }
    return studentsUpdateGrades;
  });
}
