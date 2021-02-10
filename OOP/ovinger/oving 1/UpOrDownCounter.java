package stateandbehavior;

public class UpOrDownCounter {
	
	int start;
	int end;
	int counter;
	
	public UpOrDownCounter(int start, int end) {
		this.start = start;
		this.end = end;
		counter = start;
	}
	
	public int getCounter() {
		return counter;
	}
	
	public boolean count() {
		if (counter < end) {
			counter++;
			if (counter == end) {
				return false;
			}
			return true;
		}
		if (counter > end) {
			counter--;
			if (counter == end) {
				return false;
			}
			return true;
		}
		return false;
	}
	
	
	public static void main(String[] args) {
		UpOrDownCounter c = new UpOrDownCounter(1, -2);
		
		
		System.out.println(c.getCounter());
		System.out.println(c.count());
		System.out.println(c.getCounter());
		System.out.println();

		System.out.println(c.getCounter());
		System.out.println(c.count());
		System.out.println(c.getCounter());
		System.out.println();

		System.out.println(c.getCounter());
		System.out.println(c.count());
		System.out.println(c.getCounter());
		System.out.println();

		System.out.println(c.getCounter());
		System.out.println(c.count());
		System.out.println(c.getCounter());
		System.out.println();

		System.out.println(c.getCounter());
		System.out.println(c.count());
		System.out.println(c.getCounter());
		System.out.println();

	}
	
}
