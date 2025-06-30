interface PaymentGateway {
    void processPayment(double amount);
}
class PayPalGateway implements PaymentGateway {
    public void processPayment(double amount) {
        System.out.println("Processing $" + amount + " via PayPal");
    }
}
class PaymentProcessor {
    private PaymentGateway gateway;
    public PaymentProcessor(PaymentGateway gateway) {
        this.gateway = gateway;
    }
    public void executePayment(double amount) {
        gateway.processPayment(amount);
    }
}
public class Main {
    public static void main(String[] args) {
        PaymentProcessor processor = new PaymentProcessor(new PayPalGateway());
        processor.executePayment(149.99);
    }
}
