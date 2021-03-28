package interfaces;

import java.util.Iterator;

public class StringGridIterator implements Iterator<String>{
	
	int rows;
	int cols;
	int pos = 0;
	StringGrid stringGrid;
	boolean rowMajor;

	public StringGridIterator(StringGrid stringGrid, boolean rowMajor) {
		this.rows = stringGrid.getRowCount();
		this.cols = stringGrid.getColumnCount();
		this.stringGrid = stringGrid;
		this.rowMajor = rowMajor;
	}

	@Override
	public boolean hasNext() {
		return pos < rows * cols;
	}

	@Override
	public String next() {
		String s = rowMajor ? stringGrid.getElement(pos / cols, pos % cols): stringGrid.getElement(pos % rows, pos / rows); 
		pos++;
		return s;
	}

}
