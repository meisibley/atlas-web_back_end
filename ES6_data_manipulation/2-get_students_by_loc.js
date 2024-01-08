export default function getStudentsByLocation(studentsArray, city) {
  if (!Array.isArray(studentsArray)) {
    return [];
  }
  const cityArray = studentsArray.filter((item) => item.location === city);
  return cityArray;
}
