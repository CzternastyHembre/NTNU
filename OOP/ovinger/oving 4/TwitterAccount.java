package objectstructures;

import java.util.ArrayList;
import java.util.List;

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
	
	public static void main(String[] args) {
		TwitterAccount ole = new TwitterAccount("Ole");
		TwitterAccount per = new TwitterAccount("per");
		
		ole.tweet("Twii");
		ole.tweet("Twiiiii");
		per.retweet(ole.getTweet(1));
		System.out.println(ole.getRetweetCount());
	}
}
