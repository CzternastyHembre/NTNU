package interfaces.twitter;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import interfaces.twitter.UserNameComparator;

public class TwitterAccount {
	private String userName;
	private List<TwitterAccount> followers = new ArrayList<>();
	private List<Tweet> tweets = new ArrayList<>();
	
	public TwitterAccount(String userName) {
		this.userName = userName;
	}
	
	public String getUserName() {
		return userName;
	}
	
	public boolean isFollowing(TwitterAccount account) {
		if (account.followers.contains(this)) {
			return true;
		}
		return false;
	}
	
	public boolean isFollowedBy(TwitterAccount account) {
		return account.isFollowing(this);
	}
	
	public void follow(TwitterAccount account) {
		if (!this.isFollowing(account)) {
			account.followers.add(this);
		}
	}
	
	public void unfollow(TwitterAccount account) {
		if (this.isFollowing(account)) {
			account.followers.remove(this);
		}
	}
	
	public void tweet(String text) {
		Tweet myTweet = new Tweet(this, text);
		tweets.add(0, myTweet);
	}

	public void retweet(Tweet tweet) {
		Tweet myRetweet = new Tweet(this, tweet);
		tweets.add(0, myRetweet);
	}
	
	public int getTweetCount() {
		return tweets.size();
	}
	
	public List<TwitterAccount> getFollowers(){
		return followers;
	}
	
	public List<TwitterAccount> getFollowers(Comparator<TwitterAccount> comp) {
		List<TwitterAccount> l = new ArrayList<>(this.getFollowers());
		Collections.sort(l, comp);
		return l;
		
	}
	
	public int getFollowerCount() {
		return this.followers.size();
	}
	
	public int getRetweetCount() {
		int totalre = 0;
		for (Tweet tweet : tweets) {
			totalre += tweet.getRetweetCount();
		}
		return totalre;
	}
	
	public Tweet getTweet(int i) {
		return this.tweets.get(i - 1);
	}
	
	@Override
	public String toString() {
		return this.userName + " f:" + this.getFollowers().size() + " t:" + this.getTweetCount();
	}
	
	public static void main(String[] args) {
		TwitterAccount ole = new TwitterAccount("Ole");
		TwitterAccount per = new TwitterAccount("per");
		
		ole.tweet("Twii");
		ole.tweet("Twiiiii");
		per.retweet(ole.getTweet(1));
//		System.out.println(ole.getRetweetCount());

	
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
		c.follow(b);
		
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
		

		System.out.println("\t\t" + twlst);
		
		twlst.sort(new UserNameComparator());
		
		System.out.println("Name: \t\t" + twlst);

		twlst.sort(new FollowersCountComparator());
		
		System.out.println("Followers: \t" + twlst);
		
		twlst.sort(new TweetsCountComparator());
		
		System.out.println("Tweets \t\t" + twlst);

		System.out.println();
		System.out.println(a.getFollowers() + "\n");
		System.out.println(a.getFollowers(new FollowersCountComparator()));
		System.out.println(a.getFollowers(new UserNameComparator()));
		System.out.println(a.getFollowers(new TweetsCountComparator()));
		System.out.println();
		System.out.println(a.getFollowers());
		
		System.out.println();
		System.out.println(twlst);
		Collections.sort(twlst, new TwitterAccountComparator());
		System.out.println(twlst);
	}

}
