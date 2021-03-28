package interfaces;

import java.util.Iterator;

public class StringGridImpl implements StringGrid{
	
	private int rows;
	private int cols;
	private String[][] grid;
	
	public StringGridImpl(int rows, int cols) {
		this.rows = rows;
		this.cols = cols;
		this.grid = new String[rows][cols];
		// TODO Auto-generated constructor stub
		
	}
	
	@Override
	public int getRowCount() {
		return rows;
	}

	@Override
	public int getColumnCount() {
		return cols;
	}

	@Override
	public String getElement(int row, int col) {
		return grid[row][col];
	}

	@Override
	public void setElement(int row, int col, String element) {
		this.grid[row][col] = element;
	}

	@Override
	public Iterator<String> iterator() {
		return new StringGridIterator(this, true);
	}

}
