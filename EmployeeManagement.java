public class EmployeeManagement {
    public static void main(String[] args) {
        Employee emp = new Employee("Sophia Liang", 1001);
        emp.printDetails();
        emp.setDepartment("Engineering");
        System.out.println("Department: " + emp.getDepartment());
    }
}
class Employee {
    private String name;
    private int id;
    private String department;
    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }
    public void printDetails() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
    public String getDepartment() { return department; }
    public void setDepartment(String dept) { this.department = dept; }
}
