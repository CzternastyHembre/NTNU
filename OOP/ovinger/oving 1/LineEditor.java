package stateandbehavior;

public class LineEditor {
	
	private String text = "";
	private int insertionIndex = 0;
	

	public void setText(String text) {
		this.text = text;
	}
	
	public String getText() {
		return text;
	}

	public int getInsertionIndex() {
		return insertionIndex;
	}
	
	public void setInsertionIndex(int insertionIndex) {
		this.insertionIndex = insertionIndex;
	}
	
	public void left() {
		left(1);
	}
	public void left(int n) {
		if (insertionIndex - n < 0 ) {
			insertionIndex = 0;
		} else {
			insertionIndex -= n;			
		}
	}

	public void right() {
		right(1);
	}
	
	public void right(int n) {
		if (insertionIndex + n > text.length()) {
			insertionIndex = text.length();
		} else {
			insertionIndex += n;
		}
	}
	
	public void insertString(String s) {
		String left = text.substring(0,insertionIndex);
		String right = text.substring(insertionIndex, text.length());
		text = left + s + right;
		insertionIndex += s.length();
	}
	
	public void deleteLeft() {
		if (insertionIndex > 0) {
			String left = text.substring(0,insertionIndex-1);
			String right = text.substring(insertionIndex, text.length());
			text = left + right;			
			left();
		}
	}
	
	public void deleteRight() {
		if (insertionIndex < text.length()) {
			String left = text.substring(0,insertionIndex);
			String right = text.substring(insertionIndex+1, text.length());
			text = left + right;			
		}
	}
	
	
	@Override
	public String toString() {
		String left = text.substring(0,insertionIndex);
		String right = text.substring(insertionIndex, text.length());
		return left+ "|" + right;			
		
	}
	
	
	public static void main(String[] args) {
		LineEditor text = new LineEditor();
		text.insertString("aa");
		System.out.println(text);
		
		text.right();
		text.insertString("bb");
		text.deleteLeft();
		System.out.println(text);
		
//		text.left();
//		text.insertString("cc");
//		System.out.println(text.text);
	}
	
	
	
}
