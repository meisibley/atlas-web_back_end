export default function getListStudentIds(objArray) {
  if (!(objArray instanceof Array)) {
    return [];
  }
  const idArray = [];
  idArray = objArray.map((item) => item.id);
  return idArray;
}