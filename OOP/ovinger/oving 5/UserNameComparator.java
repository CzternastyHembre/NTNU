package interfaces.twitter;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class UserNameComparator implements Comparator<TwitterAccount>{
	
	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		return o1.getUserName().compareTo(o2.getUserName());
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
		System.out.println(twlst);
		
		twlst.sort(new UserNameComparator());
		
		System.out.println(twlst);
	}

}

