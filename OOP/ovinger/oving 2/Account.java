package encapsulation;

public class Account {
	double balance;
	double interestRate;
	
	public Account(double balance, double interestRate) {
		if (balance < 0 || interestRate < 0) {
			throw new IllegalArgumentException("Not valid inputs");
		}
		this.balance = balance;
		this.interestRate = interestRate;
		// TODO Auto-generated constructor stub
	}
	
	public double getBalance() {
		return balance;
	}
	
	public double getInterestRate() {
		return interestRate;
	}
	
	
	public void setInterestRate(double interestRate) {
		if (interestRate < 0) {
			throw new IllegalArgumentException("Not valid inputs");
		}
		this.interestRate = interestRate;
	}
	
	
	public void deposit(double amount) {
		if (amount <= 0) {
			throw new IllegalArgumentException("Not valid inputs");
		}
		balance += amount;
	}
	
	public void withdraw(double amount) {
		if (amount < 0 || balance - amount < 0) {
			throw new IllegalArgumentException("Not valid inputs");
		}
		balance -= amount;
	}
	
	public void addInterest() {
		balance += interestRate;
	}
	
	
	public static void main(String[] args) {
		Account a = new Account(1, -1);
		
		System.out.println(a.interestRate);
		
	}
}
