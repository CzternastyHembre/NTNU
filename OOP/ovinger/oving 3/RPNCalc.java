package encapsulation;

import java.util.ArrayList;
import java.util.List;

public class RPNCalc {
	List<Double> Stack = new ArrayList<Double>();	
	
	public void push(double num) {
		Stack.add(num);
	}
	
	public Double pop() {
		int lastIndex = Stack.size()-1;
		if (lastIndex < 0) {
			return Double.NaN;
		}
		Double popped = Stack.get(lastIndex);
		Stack.remove(lastIndex);
		return popped;
	}
	
	public Double peek(int i) {
		int actualIndex = Stack.size()-i;
		if (actualIndex < 0 || actualIndex >= Stack.size()) {
			return Double.NaN;
		}
		return Stack.get(actualIndex);
	}
	
	public int getSize() {
		return Stack.size();
	}
	
	public void performOperation(char op) {
		Double l1 = pop();
		Double l2 = pop();
		if (op == '+') {
			Double sum = l2 + l1;
			push(sum);
		} else if (op == '-') {
			Double sum = l2 - l1;
			push(sum);	
		} else if (op == '*') {
			Double sum = l2 * l1;
			push(sum);	
		} else if (op == '/') {
			Double sum = l2 / l1;
			push(sum);
		}
	}
	
	public static void main(String[] args) {
		RPNCalc c = new RPNCalc();
		System.out.println(c);
		
	}

}
