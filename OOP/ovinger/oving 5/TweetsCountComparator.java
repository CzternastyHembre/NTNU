package interfaces.twitter;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class TweetsCountComparator implements Comparator<TwitterAccount> {

	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		return o2.getTweetCount() - o1.getTweetCount();
	}

	
	public static void main(String[] args) {
		TwitterAccount a = new TwitterAccount("ape");
		TwitterAccount b = new TwitterAccount("ball");
		TwitterAccount c = new TwitterAccount("cat");
		TwitterAccount d = new TwitterAccount("dick");
		List<TwitterAccount> twlst = new ArrayList<>();	
		twlst.add(b);
		twlst.add(a);
		twlst.add(d);
		twlst.add(c);
		
		a.tweet("AAA");
		a.tweet("AAA");
		a.tweet("AAA");
		a.tweet("AAA");
		
		c.tweet("AAA");
		c.tweet("AAA");
		c.tweet("AAA");
		
		d.tweet("AAA");
		d.tweet("AAA");

		b.tweet("AAA");

		System.out.println(twlst);
		
		twlst.sort(new TweetsCountComparator());
		
		System.out.println(twlst);

	}

	
	
}
