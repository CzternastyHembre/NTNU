package stateandbehavior;

import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class Digit {
	
	int tallSystem;
	int value;
	
	public Digit(int tallSystem) {
		this.tallSystem = tallSystem;
		value = 0;
	}
	
	public int getValue() {
		return value;
	}
	
	public boolean increment() {
		value++;
		if (value == tallSystem) {
			value = 0;
			return true;
		} else {
			return false;			
		}
	}
	
	public int getBase() {
		return tallSystem;
	}

	@Override
	public String toString() {
		List<String> tall = new ArrayList<String>();
		tall.add("0");
		tall.add("1");
		tall.add("2");
		tall.add("3");
		tall.add("4");
		tall.add("5");
		tall.add("6");
		tall.add("7");
		tall.add("8");
		tall.add("9");
		tall.add("A");
		tall.add("B");
		tall.add("C");
		tall.add("D");
		tall.add("E");
		tall.add("F");
		tall.add("G");
		tall.add("H");
		tall.add("I");
		tall.add("J");
		tall.add("K");
		tall.add("L");
		tall.add("M");
		tall.add("N");
		tall.add("O");
		tall.add("P");
		tall.add("Q");
		tall.add("R");
		tall.add("S");
		tall.add("T");
		tall.add("U");
		tall.add("V");
		tall.add("W");
		tall.add("X");
		tall.add("Y");
		tall.add("Z");
		return tall.get(value);
		// TODO Auto-generated method stub
	}
	
	public static void main(String[] args) {
		Digit t1 = new Digit(16);
		Digit t2 = new Digit(16);
		Digit t3 = new Digit(16);
		
		for (int i = 0; i < t3.getBase(); i++) {
			for (int j = 0; j < t2.getBase(); j++) {
				for (int k = 0; k < t1.getBase(); k++) {
					System.out.println(t3.toString() + "" + t2.toString() + "" + t1.toString());
					if (t1.increment()) {
						if (t2.increment()) {
							t3.increment();
						}
					}
				}
			}
		}
		System.out.println(t3.getValue() + "" + t2.getValue() + "" + t1.getValue());
	}
}
