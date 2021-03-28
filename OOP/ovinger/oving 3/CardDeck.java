package encapsulation;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CardDeck {
	List<Card> Deck = new ArrayList<Card>();
	static final char[] Suits = {'S', 'H', 'D', 'C'};
	
	public CardDeck(int n) {
		
		for (int i = 0; i < Suits.length; i++) {
			for (int j = 1; j <= n; j++) {
				Card c = new Card(Suits[i], j);
				Deck.add(c);
			}
		}
	}
	
	public int getCardCount() {
		return Deck.size();
	}
	
	public Card getCard(int n) {
		return Deck.get(n);
	}
	
	public void shufflePerfectly() {
		int half = Deck.size()/2;
		for (int i = 0; i < half; i++) {
			Deck.add(2*i+1, Deck.get(i*2+half));
		}
		Deck = Deck.subList(0, half*2);
	}
		
	public static void main(String[] args) {
		CardDeck d = new CardDeck(2);
		System.out.println(d.Deck);
//		Card c = new Card('C',5);
//		d.Deck.add(2, c);
		d.shufflePerfectly();
		System.out.println(d.Deck);
	}
}
