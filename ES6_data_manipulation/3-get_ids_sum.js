export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }
  const sum = students.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id,
  );
  return sum;
}
