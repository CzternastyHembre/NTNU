package interfaces.twitter;

import java.util.Comparator;

public class TwitterAccountComparator implements Comparator<TwitterAccount>{

	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		int o1Fcount = o1.getFollowerCount();
		int o2Fcount = o2.getFollowerCount();
		int o1Tcount = o1.getTweetCount();
		int o2Tcount = o2.getTweetCount();
		int maxL = Math.max(o1Tcount, o2Tcount);
		
		if (o1Fcount > o2Fcount) {return -1;}
		if (o1Fcount < o2Fcount) {return 1;}
		if (o1Tcount > o2Tcount) {return -1;}
		if (o1Tcount < o2Tcount) {return 1;}
		return o1.getUserName().compareTo(o1.getUserName());
	}

}
