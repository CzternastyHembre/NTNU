package interfaces.twitter;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class FollowersCountComparator implements Comparator<TwitterAccount>{
	
	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		return o2.getFollowers().size() - o1.getFollowers().size();
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
		
		b.follow(a);
		d.follow(a);
		c.follow(a);
		
		
		a.follow(c);
		b.follow(c);
		
		a.follow(b);


		
		System.out.println(twlst);
		
		twlst.sort(new FollowersCountComparator());
		
		System.out.println(twlst);


	}

}

