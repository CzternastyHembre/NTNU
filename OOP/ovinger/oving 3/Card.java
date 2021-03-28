package encapsulation;

public class Card {
	char suit;
	int face;
	
	public Card(char suit, int face) {
		if (checkFace(face) && checkSuit(suit)) {
			this.face = face;
			this.suit = suit;
		} else {
			throw new IllegalArgumentException("Illegal argument");
		}
	}
	
	private boolean checkFace(int face) {
		if (face > 0 && face < 14) {
			return true;
		}
		return false;
	}
	
	private boolean checkSuit(char suit) {
		if (suit == 'S' || suit == 'H' || suit == 'D' || suit == 'C') {
			return true;
		}
		return false;
	}
	
	public char getSuit() {
		return suit;
	}
	
	public int getFace() {
		return face;
	}
	
	@Override
	public String toString() {
		return "" + suit + face;
	}
	
	

}
