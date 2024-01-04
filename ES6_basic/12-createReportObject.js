export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.Keys(this.allEmployees).length;
    },
  };
}
