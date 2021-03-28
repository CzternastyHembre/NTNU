package objectstructures;

//import org.junit.Test;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class CoffeeCupTest {
	private CoffeeCup cup;
	

	@BeforeEach
	public void setup() {
		cup = new CoffeeCup();
	}
	
	private void checkCapacity(int capacity) {
		Assertions.assertEquals(cup.getCapacity(), capacity);
	}
	
	private void checkVolume(int volume) {
		Assertions.assertEquals(cup.getCurrentVolume(), volume);
	}
	
	@Test
	public void testGetCapacity() {
		checkCapacity(0);
	}

	@Test
	public void testGetVolume() {
		checkVolume(0);
	}
	
	@Test
	public void testIncreaseCupSize() {
		cup.increaseCupSize(10);
		checkCapacity(10);
		cup.increaseCupSize(-5);
		checkCapacity(10);
	}
	
	@Test
	public void testFillCoffee() {
		cup.increaseCupSize(10);
		cup.fillCoffee(10);
		checkVolume(10);
		
		Assertions.assertThrows(IllegalArgumentException.class , () -> cup.fillCoffee(10));
	}
	
	@Test
	public void testDrinkCoffee() {
		cup.increaseCupSize(10);
		cup.fillCoffee(10);
		cup.drinkCoffee(3);
		checkVolume(10-3);
		Assertions.assertThrows(IllegalArgumentException.class , () -> cup.drinkCoffee(10));
	}
	
	

}