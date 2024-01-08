import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(students) {
  const idList = getListStudentIds(students);
  const sum = idList.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
  );
  return sum;
}
