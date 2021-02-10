package stateandbehavior;

public class Account {
	double balance = 0;
	double interestRate = 1;
	
	public double getBalance() {
		return balance;
	}
	
	public double getInterestRate() {
		return interestRate;
	}
	
	public void setInterestRate(double interestRate) {
		this.interestRate = interestRate;
	}
	
	public void deposit(double amount) {
		if (amount > 0) {
			this.balance += amount;
		}
	}
	
	public void addInterest() {
		double interest = interestRate;
		deposit(interest);
	}
	
	@Override
	public String toString() {
		return "Du har " + balance + " på kontoen med en interestrate på " + interestRate + ".";
	}
	
	public static void main(String[] args) {
		Account a = new Account();
		a.deposit(100);
		System.out.println(a);
		a.setInterestRate(1.2);
		a.addInterest();
		System.out.println(a);
		
	}
}
