package stateandbehavior;

public class Rectangle {

	int minX;
	int minY;
	
	int maxX;
	int maxY;
	
	int height;
	int width;
	
	
	public int getMaxX() {
		return maxX;
	}
	
	public int getMaxY() {
		return maxY;
	}
	
	public int getMinX() {
		return minX;
	}
	
	public int getMinY() {
		return minY;
	}
	
	public int getHeight() {
		return maxY- minY;
	}
	
	public int getWidth() {
		return maxX - minX;
	}
	
	public boolean isEmpty() {
		return height == 1;
	}
	
	public boolean contains(int x, int y) {
		if (x >= minX && x < maxX && y >= minY && y < maxY) {
			return true;
		}
		return false;
	}
	
	public boolean contains(Rectangle rect) {
		if (contains(rect.minX, rect.minY) && contains(rect.maxX, rect.maxY)) {
			return true;
		}
		return false;
	}
	
	public boolean add(int x, int y) {
		if (!contains(x, y)) {
			minX = Math.min(x, minX);
			minY = Math.min(y, minY);
			maxX = Math.max(x, maxX) + 1;
			maxY = Math.max(y, maxY) + 1;
			return true;
		}
		return false;
	}
	
	public boolean add(Rectangle rect) {
		if (!contains(rect.minX, rect.minY) || !contains(rect.maxX, rect.maxY)) {
			add(rect.minX, rect.minY);
			add(rect.maxX, rect.maxY);
			return true;
		}
		return false;
	}
	
	//Intersection ?
	public Rectangle union(Rectangle rect) {
		int newminX = Math.max(minX, rect.minX);
		int newminY = Math.max(minY, rect.minY);
		int newmaxX = Math.min(maxX, rect.maxX);
		int newmaxY = Math.min(maxY, rect.maxY);
		Rectangle r = new Rectangle();
		r.add(newminX, newminY);
		r.add(newmaxX, newmaxY);
		return r;
	}
	
	
	
	
	
	
	
	public static void main(String[] args) {
		Rectangle r = new Rectangle();
		
		System.out.println(r.getHeight());
		System.out.println(r.getMinX());
		System.out.println(r.isEmpty());
		
	}
	
}