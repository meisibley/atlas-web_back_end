export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsLocat = students.filter((item) => item.location === city);

  // initial all students of the city grades to N/A
  for (const elem of studentsLocat) {
    elem.grade = 'N/A';
  }
  
  const studentsUpdateGrades = studentsLocat.map((items) => {
    const items1 = items; // to solve "Assignment to property of function parameter 'items' no-param-reassign"
    for (const nGrade of newGrades) {
      // if the student's id is in newGrade, update whose grade
      if (items1.id === nGrade.studentId) {
        items1.grade = nGrade.grade;
      }
    }
    return items1;
  });
  return studentsUpdateGrades;
}
